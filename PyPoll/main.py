

import os
import csv

# Set path for file
csvpath = "election_data.csv"

totalcount_1 = 0
totalcount_2 = 0
totalcount_3 = 0
totalcount_4 = 0
totalcount = 0
name1 = "Khan"
name2 = "Correy"
name3 = "Li"
name4 = "O'Tooley"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    for row in csvreader:
        totalcount = totalcount + 1

        
        if row[2] == name1:
            totalcount_1 = totalcount_1 + 1
        
        if row[2] == name2:
            totalcount_2 = totalcount_2 + 1
            
        if row[2] == name3:
            totalcount_3 = totalcount_3 + 1 
            
        if row[2] == name4:
            totalcount_4 = totalcount_4 + 1
              

print("Election Results")
print("-------------------")
print("Total Votes: " + str(totalcount))
print("-------------------")
print(name1 + ": " + str(round(totalcount_1 / totalcount * 100)) +"% " + str(totalcount_1))
print(name2 + ": " + str(round(totalcount_2 / totalcount * 100)) +"% " + str(totalcount_2)) 
print(name3 + ": " + str(round(totalcount_3 / totalcount * 100)) +"% " + str(totalcount_3))
print(name4 + ": " + str(round(totalcount_4 / totalcount * 100)) +"% " + str(totalcount_4))


print("-------------------")
if (totalcount_1 > totalcount_2) & (totalcount_1 > totalcount_3) & (totalcount_1 > totalcount_4):
    print("Winner: " + name1)
if (totalcount_2 > totalcount_1) & (totalcount_2 > totalcount_3) & (totalcount_2 > totalcount_4):
    print("Winner: " + name2)   
if (totalcount_3 > totalcount_1) & (totalcount_3 > totalcount_2) & (totalcount_3 > totalcount_4):
    print("Winner: " + name3)    
if (totalcount_4 > totalcount_1) & (totalcount_4 > totalcount_2) & (totalcount_4 > totalcount_3):
    print("Winner: " + name4)    
    
print("-------------------")

output_path = os.path.join("election.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow([name1, str(round(totalcount_1 / totalcount * 100)), str(totalcount_1)])
    csvwriter.writerow([name2, str(round(totalcount_2 / totalcount * 100)), str(totalcount_2)])
    csvwriter.writerow([name3, str(round(totalcount_3 / totalcount * 100)), str(totalcount_3)])
    csvwriter.writerow([name4, str(round(totalcount_4 / totalcount * 100)), str(totalcount_4)])
    csvwriter.writerow(["Winner: " + name1])

