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

        # Count total number of voters
        votersCount = votersCount + 1

        # Append every vote to "candidates" list
        candidates.append(str(row[2]))

# Sort candidates by name
candidates.sort()

# Initialize variables to use in for loop
oldCand = candidates[0]
candCount = 0
rowCount=0
pollDicts = []

# Create list of dictionaries for each candidate and their respective vote totals
for row in candidates:
    rowCount = rowCount + 1
    if row != oldCand or rowCount == votersCount:
        num = candidates.count(oldCand)
        pollDicts.append({"Candidate":oldCand, "Votes":num})
        oldCand = row

# votes function returns vote totals   
def votes(v):
    return v['Votes']
# Use votes function to sort dictionaries by vote totals
pollDicts.sort(reverse = True, key=votes)

# print(line1)
lineTotal = f"Total:\t\t{votersCount}"


text = f"{lineTotal} \n-----------------------------"
# for each dictionary, print candidate's name, vote total, and percent of total votes
for dict in pollDicts:
    percent = round((dict['Votes']/votersCount)*100)
    can = dict['Candidate']
    v = dict['Votes']
    if len(dict['Candidate'])>7:
        tab = "\t"
    else:
        tab = "\t\t"
    lineCandidate = f"\n{can}:{tab}{v}\t({percent}%)"

    text=text+f"{lineCandidate}"
winner=pollDicts[0]['Candidate']
lineWinner=f"Winner:\t\t{winner}"

text=text+"\n-----------------------------\n"+ lineWinner
# Write analysis to text file
print(text)
with open("PyPoll.txt", "w") as file:
    file.write(f"{text}")
