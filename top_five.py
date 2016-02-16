import csv
from collections import Counter
import operator

def top_five_teams(myFile):
    f = open(myFile)
    csv_f = csv.reader(f)

    teams = []
    wins = []
                        #Creates a list of teams
    for row in csv_f:
        if row[4] not in teams:
            teams.append(row[4])
    teams.remove('Winner/tie')
                        #Calculates the number of wins for every team
    for team in teams:
        f.seek(0)
        counter = 0
        for row in csv_f:
            if row[4] == team:
                counter += 1
        wins.append(counter)
                        #Creates key-value pairs of teams and wins
    record = dict(zip(teams, wins))
                        #Makes a list of the best 5 teams
    top_five = []
    counter = 0
    while(counter < 6):
        x = max(record.iterkeys(), key=lambda k: record[k])
        top_five.append(x)
        record.pop(x)
        counter += 1

    return(top_five)
