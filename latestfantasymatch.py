import requests

liveMatchUrl = 'https://s3-ap-southeast-1.amazonaws.com/images-fantasy-iplt20/match-data/livematch.json'

def getLatestMatchData():
    #Make request
    r = requests.get(liveMatchUrl)

    #Obtain live match data
    latestMatchData = r.json()

    #Store matchId (Obtains the first(aka latest/live) match details and extracts matchId)
    #matchId = next(iter(latestMatchData['matchInfo']))

    #Get matchId
    matchId = latestMatchData['liveMatchId']

    #Return latest matchId and matchKey
    return {'matchId': str(matchId) , 'matchKey': latestMatchData['matchInfo'][str(matchId)]['matchKey']}
