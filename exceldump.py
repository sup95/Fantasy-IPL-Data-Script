import xlsxwriter
from terminalcolors import terminalcolors

def dumpDataInExcel(prettyData, matchKey):

    # Create workbook and add worksheet.
    workbook = xlsxwriter.Workbook('FantasyIPLData_Match' + matchKey + '.xlsx')
    worksheet = workbook.add_worksheet()

    row = 0
    worksheet.write(row, 0, 'Player Id')
    worksheet.write(row, 1, 'Player Name')
    worksheet.write(row, 2, 'Bat')
    worksheet.write(row, 3, 'Bowl')
    worksheet.write(row, 4, 'Field')
    worksheet.write(row, 5, 'Total')

    row = 1

    for playerScoreData in prettyData:
        worksheet.write(row, 0, getattr(playerScoreData, 'playerId'))
        worksheet.write(row, 1, getattr(playerScoreData, 'playerName'))
        worksheet.write(row, 2, getattr(playerScoreData, 'batScore'))
        worksheet.write(row, 3, getattr(playerScoreData, 'bowlScore'))
        worksheet.write(row, 4, getattr(playerScoreData, 'fieldScore'))
        worksheet.write(row, 5, getattr(playerScoreData, 'totalScore'))

        row += 1

    print(terminalcolors.OKGREEN + "Data added to FantasyIPLData_Match" + matchKey +  " workbook. :) " + terminalcolors.ENDCOLOR)

    workbook.close()
