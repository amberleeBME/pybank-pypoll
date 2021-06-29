# Instructions
# 1. Read CSV file
# 2. Calculate:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period
 # 3. Print analysis to the terminal
 # 3. Export a text file with the results
#-----------------------------------------------------------------------------

# Define variables
months = 0
net = 0
delta = []
avg = 0
inc = 0
dec = 0

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

        #Count the number of months
        months = months + 1 

        #Calculate net total
        net = net + (int(row[1]))

        #Calculate monthly change and append to list
        if months > 1:
            delta.append(int(row[1])-prev)

        # Store current month's profit/loss
        prev = int(row[1])

# Calculate average monthly change
avg = round(sum(delta)/len(delta),2)

# Calculate max monthly change
inc = max(delta)

# Calculate min monthly change
dec = min(delta)



# Print analysis to terminal
print(f"Total Number of months: {months}")
print(f"Net Total: ${net}")
print(f"Average change: ${avg}")
print(f"Greatest increase: ${inc}")
print(f"Greatest decrease: ${dec}")