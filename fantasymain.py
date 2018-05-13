import sys
from collections import namedtuple

import fantasylogin
import latestfantasymatch
import fantasylivescore
import fantasyplayerdata
import wranglefantasydata
import exceldump
from terminalcolors import terminalcolors


################################### Login and stuff ###################################

if(len(sys.argv) == 3):
    userId = sys.argv[1]
    password = sys.argv[2]
else:
    print (terminalcolors.WARNING + 'Please re-run script with userid and password as script arguments.' + terminalcolors.ENDCOLOR)
    sys.exit()

#Login
loginResultData = fantasylogin.login(userId, password)

#Print login status
print(terminalcolors.OKGREEN + loginResultData['loginStatus'] + terminalcolors.ENDCOLOR)

#Store access token.
accessToken = loginResultData['accessToken']


################################### Latest match data ###################################

#Get latest fantasy match details
latestMatchData = latestfantasymatch.getLatestMatchData()

#Store matchId and matchKey
matchId = latestMatchData['matchId']
matchKey = latestMatchData['matchKey']


################################### The Crux: Livescore ###################################

#liveScoreData contains array of objects containing playerIds and their respective scores.
liveScoreData = fantasylivescore.getLiveScore(userId, matchId, matchKey, accessToken)


################################### Player Data ###################################

#allPlayersData contains player data for both teams of a particular match.
allPlayersData = fantasyplayerdata.getPlayerData(matchKey)


################################### Data Wrangling ###################################

PlayerLiveScores = namedtuple('PlayerLiveScores', 'playerId playerName batScore bowlScore fieldScore totalScore')

prettyData = wranglefantasydata.wrangleFantasyData(PlayerLiveScores, allPlayersData, liveScoreData)


################################### Dump in Excel ###################################

exceldump.dumpDataInExcel(prettyData, matchKey)
