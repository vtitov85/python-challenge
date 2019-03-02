import os
import csv

# Set path for file
csvpath = "Desktop/election_data.csv"

totalcount = 0
votes = {}
maxVotes = 0

logFile=open('output.log','w')

def log(text):
    print(text)
    if logFile:
        logFile.write(str(text) + "\n")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    for row in csvreader:
        totalcount += 1
        candidate = row[2]
        if not candidate in votes:
            votes[candidate] = 0
        votes[candidate] += 1

log("Election Results")
log("-------------------")
log("Total Votes: " + str(totalcount))
log("-------------------")
for k, v in votes.items():
    if v > maxVotes:
        winner = k
        maxVotes = v        
    log(str(k) + ": " + format(v * 100/totalcount, '.3f') + "%(" + str(v) + ")")
log("-------------------")
log("Winner: " + winner)
log("-------------------")

logFile.close()
