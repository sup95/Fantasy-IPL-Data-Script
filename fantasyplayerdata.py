import requests
import json

#Get player data for both teams of a given match.
def getPlayerData(matchKey):
    playerDataUrl = ("https://datacdn.iplt20.com/dynamic/data/core/cricket/2012/ipl2018/ipl2018-" + matchKey +
                    "/scoring.js?onScoring=__jp0")

    r = requests.get(playerDataUrl)

    #Convert to Json
    playerData = json.loads(getJsonCompatiblePlayerData(r.text))

    return playerData['matchInfo']['teams']


#Response is of the format: 'onScoring(<lot of json>);'
#Slice out the start and end of the response text to obtain valid json.
def getJsonCompatiblePlayerData(responseText):
    startText = 'onScoring('
    endText = ');'
    return responseText[len(startText):-len(endText)]
