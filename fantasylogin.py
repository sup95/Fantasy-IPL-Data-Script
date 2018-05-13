import sys
import requests
import json
from terminalcolors import terminalcolors

loginUrl = 'https://2fjfpxrbb3.execute-api.ap-southeast-1.amazonaws.com/production/userapi/authenticateuser'

def login(userId, password) :
    #Prepare payload for login.
    loginPayload = {'user_id': userId, 'password' : password}

    #Make login request
    r = requests.post(loginUrl, json.dumps(loginPayload))

    #Obtain login result json
    loginResultData = r.json()

    if 'code' in loginResultData and loginResultData['code'] == 900:
        return {'loginStatus' : loginResultData['message'], 'accessToken' : loginResultData['data']['access_token']}
    else:
        print (terminalcolors.ERROR + "Authentication failed!" + terminalcolors.ENDCOLOR)
        sys.exit()
