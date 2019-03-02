import os
import csv


# Set path for file
csvpath = "Desktop/Budget_data.csv"


revenueSum = 0
totalcount = 0
maxvalue = 0
minvalue = 0
maxdate = None
mindate = None


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    
    
    
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    for row in csvreader:
        totalcount = totalcount + 1
        revenueSum  = revenueSum + float(row[1])
        average = round(revenueSum/totalcount)
        
        if maxvalue < float(row[1]): 
            maxvalue = float (row[1])
            maxdate = row[0]
            
        if minvalue > float(row[1]): 
            minvalue = float (row[1])
            mindate = row[0]
             
print ("Financial Analysis")
print ("-------------------")
print ("Total Months: " + str(totalcount))
print ("Total: " + str(revenueSum))   
print ("Average Profit: " +str(average))
print ("Greatest Profit: " + maxdate +" "+str(maxvalue))
print ("Greatest Losses: " + mindate +" "+str(minvalue))

output_path = os.path.join("Desktop", "profit.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Criteria', 'Value'])
    csvwriter.writerow(['Total Months', str(totalcount)])
    csvwriter.writerow(['Total', str(revenueSum)])
    csvwriter.writerow(['Average Profit', str(average)])
    csvwriter.writerow(['Greatest Profit', maxdate +" "+str(maxvalue)])
    csvwriter.writerow(['Greatest Losses', mindate +" "+str(minvalue)])
