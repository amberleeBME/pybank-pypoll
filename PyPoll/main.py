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

#Import os and csv module 
import os
import csv

# Access "../Resources/election_data.csv"
csvpath = os.path.join('Resources', 'election_data.csv')