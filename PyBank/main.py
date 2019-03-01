import os
import csv


# Set path for file
csvpath = "Desktop/Budget_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvpath)
    
    #print(csvreader)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
print ("Financial Analysis")
print ("-------------------")

monthCount = 0
revenueSum = 0

row= [ rows in csvreader]

for row in csvreader:
    count(Date)
    
        count += 1
print (count)   

column = 3 
for column in csvreader:
    minimum= min(column)
print (minimum)

   
        
reader_file = csv.reader(csvpath)
value = len(list(reader_file))
print (value)


for column in csvreader:
    count += 1

average_change = value/count
print (average_change)


print ("Total Months: " + str(count))




for column in csvreader:
    sum += int(column[1])
    
print (sum)
  
print ("Total : " + str(sum))



for column in csvreader:
    maximum = max (column[1])
print (maximum)
