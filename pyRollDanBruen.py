import os
import csv
from collections import Counter

#Set file path
election_data_csv = os.path.join('.', "Resources", "election_data.csv")
# Set an output path for the text file .txt
text_path = "output.txt"

# now improve the reading using the csv module
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

# Set Variables
vote_Count = Counter() #counts the votes for each candidate 
total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

Khan_percent = Khan_votes/total_votes
Correy_percent = Correy_votes/total_votes
Li_percent = Li_votes/total_votes
OTooley_percent = OTooley_votes/total_votes

# A complete list of candidates who received votes
candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]
print(candidate_list)

# The total number of votes cast
total_votes = len(candidate_list)

# The percentage of votes each candidate won
for row in csvreader:
    candidate_list.append(row[2])

# The total number of votes each candidate won
for name in candidate_list:
    vote_Count[name] += 1

winner = max(zip(vote_Count.values(), vote_Count.keys()))

# The winner of the election based on popular vote.

# Print the election results summary
answer.append("Election Results")
answer.append("_______________________")