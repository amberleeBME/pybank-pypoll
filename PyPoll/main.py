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

    # Initialize variables
    votersCount = 0
    candidates = []
    # Read each row of data after the header
    for row in csvreader:
        # Count voter
        votersCount = votersCount + 1

        # Append candidate's name to list
        candidates.append(str(row[2]))
line1 = f"Total Votes: {votersCount}"
# Sort candidates by name
candidates.sort()

# Initialize variables
oldCand = candidates[0]
candCount = 0
distinctCands = [oldCand]
finalCount = []
rowCount=0
# pollDict = dict.fromkeys(distinctCands, finalCount)
pollDicts = []

for row in candidates:
    rowCount = rowCount + 1
    if row != oldCand or rowCount == votersCount:
        pollDicts.append({"Candidate":oldCand, "Votes":candCount})
        distinctCands.append(row)
        finalCount.append(candCount)
        candCount = 1
        oldCand = row
    else:
        candCount = candCount + 1
        
def votes(v):
    return v['Votes']

# pollDict = dict.fromkeys(distinctCands, finalCount)
# print(line1)
print(line1)
pollDicts.sort(reverse = True, key=votes)
print(pollDicts)
# Write analysis to text file
# with open("PyPoll.txt", "w") as file:
#     file.write(candidates[2])