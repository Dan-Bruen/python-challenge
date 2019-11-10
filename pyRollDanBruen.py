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

    for row in csvreader:
        total_votes += 1
        if row[2] == "Khan":
            Khan_votes +=1
        elif row[2] == "Correy":
            Correy_votes +=1
        elif row[2] == "O'Tooley":
            OTooley_votes +=1
        else:
            Li_votes +=1

# The percentage of votes each candidate won
Khan_percent = Khan_votes/total_votes
Correy_percent = Correy_votes/total_votes
Li_percent = Li_votes/total_votes
OTooley_percent = OTooley_votes/total_votes

# A complete list of candidates who received votes
candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]
print(candidate_list)

# The total number of votes cast
print(total_votes)

# The total number of votes each candidate won
print(Khan_votes)
print(Correy_votes)
print(Li_votes)
print(OTooley_votes)

# The winner of the election based on popular vote and %
## create an empty list for the candidate and his/her votes
candidates = []
num_votes = [] #number of votes for each cand
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1)) #this is vote % list
#zip candidates, num_votes and vote_percent into tuples
clean_list = list(zip(candidates, num_votes, vote_percent))
#create a winner list
winner_list = []
for name in clean_list:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])


# Election Results

print("Election Results")
print("_____________________")
print(f"Total Votes: {total_votes}")
print("_____________________")
print(f"Khan: {Khan_percent} {Khan_votes}")
print(f"Correy: {Correy_percent} {Correy_votes}")
print(f"Li: {Li_percent} {Li_votes}")
print(f"O'Tooley: {OTooley_percent} {OTooley_votes}")
print("_____________________")
print(f"Winnder: Khan")
print("_____________________")

# Export a text file with the results...
text_path = "output.txt"
saved_file = election_data_csv.strip(".csv") + text_path
file_path = os.path.join(".", saved_file)
with open(file_path, "w") as text:
    text.write("Election Results")
    text.write("_________________________")
    text.write(f"Total Votes: {total_votes}")
    text.write("_________________________")
    text.write(f"Khan: {Khan_percent} {Khan_votes}")
    text.write(f"Correy: {Correy_percent} {Correy_votes}")
    text.write(f"Li: {Li_percent} {Li_votes}")
    text.write(f"O'Tooley: {OTooley_percent} {OTooley_votes}")
    text.write("_____________________")
    text.write(f"Winnder: Khan")
    text.write("_____________________")
    