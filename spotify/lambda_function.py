import requests
import logging
import boto3
import base64

# Public string identifying our Spotify app
spotifyClientId = '5d01a10f2ad7422ebe8e97b71aa1cb11'

# First, configure logging
log = logging.getLogger()
# Remove extra handlers added by AWS Lambda so we can log our own stuff
if log.handlers:
    for handler in log.handlers:
        log.removeHandler(handler)
# Log formatting!
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)


# Invoked by AWS lambda
def lambda_handler(event, context):
    log.info("lambda_function start")

    #debug logs for now
    log.info(event)
    log.info(event['clickType'])
    inputClickType = event['clickType']
    log.info(context)


    # Initialize Systems Manager client
    ssm = boto3.client('ssm')
    # Retrieve spotify refresh token from Parameter Store
    parameter = ssm.get_parameter(Name='spotify.dash-button-scripts.refreshToken', WithDecryption=True)
    refreshToken = parameter['Parameter']['Value']


    accessToken = refreshSpotifyAccessToken(refreshToken)
    log.info(accessToken)

    headers = {'Authorization': 'Bearer ' + accessToken, 'Content-Type': 'application/json', 'Accept': 'application/json'}


    r = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)

    if r.status_code == requests.codes.ok:

        log.info(r.json())

        log.info(r.json()['item']['name'])
        log.info(r.json()['item']['uri'])

        # If the user did a single click,
        # save the current song to Angela2020 playlist
        if inputClickType == 'SINGLE':
            log.info('single click; save the song to Angela2019')
            songUri = r.json()['item']['uri']

            if songUri:
                jsonPayload = {'uris': [songUri]}

                r = requests.post('https://api.spotify.com/v1/playlists/6c0212F4lnghWrAdPY4Aku/tracks', json=jsonPayload, headers=headers)

                log.info(r.text);

        elif inputClickType == 'DOUBLE':
            log.info('double click; save the album')
            albumId = r.json()['item']['album']['id']

            if albumId:
                log.info(albumId)
                jsonPayload = [albumId]
                log.info(jsonPayload)
                r = requests.put('https://api.spotify.com/v1/me/albums', json=jsonPayload, headers=headers)

        #What is the corret text for long press?
        # elif inputClickType == "LONG"
            # What should we do here?

        else:
            log.error('invalid click type input!?')
            log.error(event)
            log.error(context)

    elif r.status_code == requests.codes.no_content: # if not a 200 OK response
        # Everything is fine, just no currently playing song!
        # We could get the last played song here, not yet implemented
        log.info("The return code from Spotify.CurrentlyPlaying was " + str(r.status_code))
        log.info("No action to take. Not a problem, carry on!")

    else: # Some other code, oh no!
        log.error("The return code from Spotify.CurrentlyPlaying was " + str(r.status_code))
        log.error(r.json());


# The token required for Spotify authentication expires after 1 hour.
# This function calls Spotify to get a new one.
# Ideally, we should store the last refresh time and only call this when the
# token has expired. 
def refreshSpotifyAccessToken(refreshToken):
    # Retrieve the Spotify application Client Secret from Parameter Store
    # https://medium.com/@nqbao/how-to-use-aws-ssm-parameter-store-easily-in-python-94fda04fea84
    ssm = boto3.client('ssm')
    parameter = ssm.get_parameter(Name='spotify.dash-button-scripts.client-secret', WithDecryption=True)
    
    log.info("Parameter store returned object:")
    log.info(parameter)

    spotifyClientSecret = parameter['Parameter']['Value']

    log.info("Parameter store returned Client Secret:")
    log.info(spotifyClientSecret);

    base64ClientIdClientSecret = base64.b64encode((spotifyClientId + ':' + spotifyClientSecret).encode('ascii'))

    log.debug('base64 "clientId:clientSecret"')
    log.debug(base64ClientIdClientSecret)

    data = {'grant_type': 'refresh_token', 'refresh_token': refreshToken}

    authHeader = 'Basic ' + base64ClientIdClientSecret.decode('ascii')
    headers = {'Authorization': authHeader}
    p = requests.post('https://accounts.spotify.com/api/token', data=data, headers=headers)

    spotifyToken = p.json()

    # We should store the access token's expiration time and only refresh the
    # token when that expiration time is up.
    # Place the expiration time (current time + almost an hour), and access token into the DB
    # table.put_item(Item={'spotify': 'prod', 'expiresAt': int(time.time()) + 3200,
                                        # 'accessToken': spotifyToken['access_token']})
    accessToken = spotifyToken['access_token']

    return accessToken