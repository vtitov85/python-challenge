import os
import csv


# Set path for file
csvpath = "Desktop/Budget_data.csv"


revenueSum = 0
totalcount = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    for row in csvreader:
        totalcount = totalcount + 1
        revenueSum  = revenueSum + float(row[1])
        average = round(revenueSum/totalcount)
    
print ("Financial Analysis")
print ("-------------------")
print ("Total Months: " + str(totalcount))
print ("Total: " + str(revenueSum))   
print ("Average Profit: " +str(average))
