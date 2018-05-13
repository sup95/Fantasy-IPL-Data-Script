import requests

def getLiveScore(userId, matchId, matchKey, accessToken):
    liveScoreUrl = ("https://2fjfpxrbb3.execute-api.ap-southeast-1.amazonaws.com/" +
                    "production/useriplapi/getlivescore?matchId=" + matchId +
                    "&userid=" + userId +
                    "&matchLink=http://datacdn.iplt20.com/dynamic/data/core/cricket/2012/ipl2018/ipl2018-" + matchKey + "/scoring.js")

    customHeadersPayload = {'userid': userId , 'accesstoken': accessToken}

    r = requests.get(liveScoreUrl, headers = customHeadersPayload)

    liveScoreData = r.json()

    return liveScoreData['data']['playerPoints']
