# Instructions
    # 1. Read CSV file
    # 2. Calculate:
        # The total number of months included in the dataset
        # The net total amount of "Profit/Losses" over the entire period
        # The average of the changes in "Profit/Losses" over the entire period
        # The greatest increase in profits (date and amount) over the entire period
        # The greatest decrease in losses (date and amount) over the entire period
    # 3. Print analysis to the terminal
    # 4. Export a text file with the results
#----------------------------------------------------------------------------------

# Initialize variables
monthCount = 0
net = 0
delta = []
months = []
analysis = []

#Import os and csv module 
import os
import csv

# Access "../Resources/budget_data.csv"
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        #Count the number of monthCount
        monthCount = monthCount + 1 

        #Calculate net total
        net = net + (int(row[1]))

        #Calculate monthly change and append to list
        if monthCount > 1:
            months.append(row[0])
            delta.append(int(row[1])-prev)

        # Store current month's profit/loss
        prev = int(row[1])

# Calculate average monthly change
avg = round(sum(delta)/len(delta),2)

# Calculate max monthly change
inc = max(delta)
maxInd = delta.index(inc)
maxMonth = months[maxInd]

# Calculate min monthly change
dec = min(delta)
minInd = delta.index(dec)
minMonth = months[minInd]

# Print analysis to terminal
print(f"Total Months: {monthCount}")
print(f"Net Total: ${net}")
print(f"Average Change: ${avg}")
print(f"Greatest Increase in profits: {maxMonth} (${inc})")
print(f"Greatest Decrease in profits: {minMonth} (${dec})")

# Convert analysis to list
analysis.append(f"Total Months: {monthCount}\n")
analysis.append(f"Net Total: ${net}\n")
analysis.append(f"Average Change: ${avg}\n")
analysis.append(f"Greatest Increase in profits: {maxMonth} (${inc})\n")
analysis.append(f"Greatest Decrease in profits: {minMonth} (${dec})\n")

# Write analysis to text file
csvpath = os.path.join('Analysis', 'PyBank.txt')
with open(csvpath, "w") as file:
    file.writelines(analysis)