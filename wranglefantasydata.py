def wrangleFantasyData(PlayerLiveScores, allPlayersData, liveScoreData):

    prettyData = []

    for team in range(0,2):
        for player in allPlayersData[team]['players']:
            playerId = player['id']
            playerName = player['fullName']
            for scoreData in liveScoreData:
                if scoreData['playerId'] == playerId:
                    batScore = scoreData['battingPoints'] #+ scoreData['secondInningBattingPoints']
                    bowlScore = scoreData['bowlingPoints'] #+ scoreData['secondInningBowlingPoints']
                    fieldScore = scoreData['fieldingPoints'] #+ scoreData['secondInningFieldingPoints']
                    playerLiveScore = PlayerLiveScores(playerId, playerName,
                                        batScore, bowlScore, fieldScore,
                                        batScore + bowlScore + fieldScore
                                        )

                    prettyData.append(playerLiveScore)

                    break

    return prettyData
