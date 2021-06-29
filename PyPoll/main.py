# Instructions
    # 1. Analyze the votes and calculate:
        # The total number of votes cast
        # A complete list of candidates who received votes
        # The percentage of votes each candidate won
        # The total number of votes each candidate won
        # The winner of the election based on popular vote.
    # 2. Print the analysis to the terminal 
    # 3. Export a text file with the results
# ---------------------------------------------------------

# Variables
votersCount = 0

# Import os and csv module 
import os
import csv

# Access "../Resources/election_data.csv"
csvpath = os.path.join('Resources', 'election_data.csv')

# Read CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        votersCount = votersCount + 1

line1 = f"Total Votes: {votersCount}"
print(line1)

# Write analysis to text file
# with open("PyPoll.txt", "w") as file:
#     file.writelines(analysis)