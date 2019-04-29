import requests
import logging
import boto3
import base64

spotifyClientId = '5d01a10f2ad7422ebe8e97b71aa1cb11'


log = logging.getLogger()
if log.handlers:
    for handler in log.handlers:
        log.removeHandler(handler)
logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)

def httpTest(event, context):


    
    log.info("function start")


    #debug logs for now
    log.info(event)
    log.info(event['clickType'])
    inputClickType = event['clickType']
    log.info(context)




    ssm = boto3.client('ssm')
    parameter = ssm.get_parameter(Name='spotify.dash-button-scripts.refreshToken', WithDecryption=True)
    refreshToken = parameter['Parameter']['Value']


    accessToken = refreshTheToken(refreshToken)
    log.info(accessToken)

    headers = {'Authorization': 'Bearer ' + accessToken, 'Content-Type': 'application/json', 'Accept': 'application/json'}


    r = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)



    if r.status_code == requests.codes.ok:

        log.info(r.json())

        log.info(r.json()['item']['name'])
        log.info(r.json()['item']['uri'])

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

    else:
        log.error('invalid click type input!?')



def refreshTheToken(refreshToken):
    #ssm parameter store
    #https://medium.com/@nqbao/how-to-use-aws-ssm-parameter-store-easily-in-python-94fda04fea84
    ssm = boto3.client('ssm')
    parameter = ssm.get_parameter(Name='spotify.dash-button-scripts.client-secret', WithDecryption=True)
    
    log.info('sam sam sam')
    log.info(parameter)
    spotifyClientSecret = parameter['Parameter']['Value']


    base64ClientIdClientSecret = base64.b64encode((spotifyClientId + ':' + spotifyClientSecret).encode('ascii'))

    log.info('base64 client secret stuff')
    log.info(base64ClientIdClientSecret)

    clientIdClientSecret = 'Basic ' + base64ClientIdClientSecret.decode('ascii')

    data = {'grant_type': 'refresh_token', 'refresh_token': refreshToken}

    headers = {'Authorization': clientIdClientSecret}
    p = requests.post('https://accounts.spotify.com/api/token', data=data, headers=headers)

    spotifyToken = p.json()

    # Place the expiration time (current time + almost an hour), and access token into the DB
    # table.put_item(Item={'spotify': 'prod', 'expiresAt': int(time.time()) + 3200,
                                        # 'accessToken': spotifyToken['access_token']})
    accessToken = spotifyToken['access_token']

    return accessToken