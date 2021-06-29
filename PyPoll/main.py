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

# Import os and csv modules
import os
import csv

# Access "../Resources/election_data.csv"
csvpath = os.path.join('Resources', 'election_data.csv')

# Read CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read and store the header row
    csv_header = next(csvreader)

    # Initialize variables
    votersCount = 0
    candidates = []

    # Read each row of data after the header
    for eachRow in csvreader:

        # Count total number of voters
        votersCount = votersCount + 1

        # Append every vote to "candidates" list
        candidates.append(str(eachRow[2]))

# Sort candidates by name
candidates.sort()

# Initialize variables to use in for loop
oldCand = candidates[0]
candCount = 0
rowCount=0
pollDicts = []

# Create list of dictionaries for each candidate and their respective vote totals
for eachVote in candidates:
    rowCount = rowCount + 1
    if eachVote != oldCand or rowCount == votersCount:
        num = candidates.count(oldCand)
        pollDicts.append({"Candidate":oldCand, "Votes":num})
        oldCand = eachVote

# votes function returns vote totals   
def votes(v):
    return v['Votes']
# Use votes function to sort dictionaries by vote totals
pollDicts.sort(reverse = True, key=votes)

# print(line1)
lineTotal = f"Total\t{votersCount}"
print("-----------------------------")
text = f"{lineTotal} \n-----------------------------"
print(text)

# for each dictionary, print candidate's name, vote total, and percent of total votes
for eachDict in pollDicts:
    percent = round((eachDict['Votes']/votersCount)*100)
    can = eachDict['Candidate']
    v = eachDict['Votes']

    if len(eachDict['Candidate'])>7:
        print(f"{can}:{v}\t({percent}%)")
    else:
        print(f"{can}:\t{v}\t({percent}%)")
        
    lineCandidate = f"\n{can}:\t{v}\t({percent}%)"
    text=text+f"{lineCandidate}"

winner=pollDicts[0]['Candidate']
lineWinner=f"-----------------------------\nWinner:\t{winner}"
print(lineWinner)
print("-----------------------------")
text=text+ "\n"+lineWinner

# Write analysis to text file

with open("PyPoll.txt", "w") as file:
    file.write(f"{text}")
