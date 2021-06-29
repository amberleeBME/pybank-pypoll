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

#Import os module 
import os

# Import csv module 
import csv

# Access "../Resources/budget_data.csv"
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Read CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)