# dash-button-scripts
Various scripts to use with AWS lambda and a Dash Button

# Development
1. Edit a .py file in subdirectory of the main repo.
2. Upload that file to AWS Lambda using the build.sh script. Ex. ./build.sh phoneSample

https://stackoverflow.com/questions/40741282/cannot-use-requests-module-on-aws-lambda
How to install libraries for use on aws lambda










 access code
     https://accounts.spotify.com/authorize?client_id=5d01a10f2ad7422ebe8e97b71aa1cb11&response_type=code&redirect_uri=http://localhost/callback&scope=user-read-currently-playing%20user-read-playback-state%20playlist-modify-public%20playlist-modify-private%20user-library-modify
 AQCM0Ckmh8tYyMg6_SCkdHfA1Q4GNc-aYnqoCQLX1oSd6MsC7NBnkq8enLVJO71LaRfJfZpDVOkA2gR7iCq_D1ZTbW8t9Erh2lgkp0gzPp4IlqO525iXYJKrHWm9YFKFX7neRJVrxhXwQC_5le6jOYbKDY-MnQVt9UrETHGJlEPfi23kJj69AutYFHaety8C3yyziC7d-sk_dryOzuA11l3XwW-P9MOMeZE-nvGRNIeMNH_cjVeuv6KhZoXmRykN8DGXxN5NgWoOgbk1toEFyRnLM6lyO-2ZOMIV01PvNCCVWe44nFGloDXLaHCScE77nFiSHAoYzBebolk0aMmNvEcTW22bKuWy5ZY5agcH



 base64 app token
     echo -n 5d01a10f2ad7422ebe8e97b71aa1cb11:6d0eb2dd68344a5c933f188a5ba017b0 | base64 
 NWQwMWExMGYyYWQ3NDIyZWJlOGU5N2I3MWFhMWNiMTE6NmQwZWIyZGQ2ODM0NGE1YzkzM2YxODhhNWJhMDE3YjA=

curl -H "Authorization: Basic NWQwMWExMGYyYWQ3NDIyZWJlOGU5N2I3MWFhMWNiMTE6NmQwZWIyZGQ2ODM0NGE1YzkzM2YxODhhNWJhMDE3YjA" -d grant_type=authorization_code -d code=AQCM0Ckmh8tYyMg6_SCkdHfA1Q4GNc-aYnqoCQLX1oSd6MsC7NBnkq8enLVJO71LaRfJfZpDVOkA2gR7iCq_D1ZTbW8t9Erh2lgkp0gzPp4IlqO525iXYJKrHWm9YFKFX7neRJVrxhXwQC_5le6jOYbKDY-MnQVt9UrETHGJlEPfi23kJj69AutYFHaety8C3yyziC7d-sk_dryOzuA11l3XwW-P9MOMeZE-nvGRNIeMNH_cjVeuv6KhZoXmRykN8DGXxN5NgWoOgbk1toEFyRnLM6lyO-2ZOMIV01PvNCCVWe44nFGloDXLaHCScE77nFiSHAoYzBebolk0aMmNvEcTW22bKuWy5ZY5agcH -d redirect_uri=http://localhost/callback https://accounts.spotify.com/api/token

{"access_token":"BQDUAhpSic62hnRl3NQb8vFqQ2_dDWm4DpC9g5pcD4h-vKbaWOWMghv_9enYW69GGFDFM_SheZbdWMk7gUT-aaGf67eCBtpmoare95QPKG10AZ_OriHPS3JPZTIt8-0yqF47NArUoKz27_92yC3gy8GmloVKRlTehxJGgDPTaU4rSuXQYiJQlSe6qvVsnn_0B5VmwP1c8YqvUX48ma5osCUZD1j9Ug","token_type":"Bearer","expires_in":3600,"refresh_token":"AQAvRlRf9BXYhpvKUe2fA-TF6zSdb41GYgEg1R4ZlmOmZ56vgdnHPn3hBNaS-twMDQD54VkiZJEyyVKD3BN0kNOcS3mfDDmCaYIe7_PV3ci6X_dI2zc6Mc8k-ynHwOlMaViqxw","scope":"user-library-modify playlist-modify-private playlist-modify-public user-read-playback-state user-read-currently-playing"}


https://docs.python.org/2/library/base64.html

 https://joshspicer.com/spotify-now-playing




https://medium.freecodecamp.org/aws-lambda-offering-developers-ultimate-flexibility-d8939ff4220

https://developer.spotify.com/documentation/web-api/reference/playlists/add-tracks-to-playlist/


https://developer.spotify.com/documentation/web-api/reference/player/get-the-users-currently-playing-track/
https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids
https://developer.spotify.com/documentation/web-api/reference/library/save-albums-user/


https://2.python-requests.org//en/master/

https://2.python-requests.org//en/master/user/quickstart/#make-a-request
