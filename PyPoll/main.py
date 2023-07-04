import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')


# Read in the CSV file
with open( election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    data = list(csvreader)

    # To calculate total votes cast
    total_votes = len(data)

    # To calculate The total number of votes each candidate won
    candidates_votes = {}
    for row in data:
        candidate = row[2]
        if candidate in candidates_votes:
            candidates_votes[candidate]["votes"] += 1
        else:
            candidates_votes[candidate] = {"votes": 1}

# To calculate The percentage of votes each candidate won
for candidate in candidates_votes:
    votes = candidates_votes[candidate]["votes"]
    percentage = (votes/total_votes) * 100
    candidates_votes[candidate]["percentage"] = round(percentage, 3)

# To get The winner of the election based on popular vote
new_votes_dict = candidates_votes
max_candidate = []
max_vote = 0
for candidate, new_votes_dict in new_votes_dict.items():
    for votes in new_votes_dict.items():
        if votes[1] > max_vote:
            max_vote = votes[1]
            max_candidate = [candidate, votes[1]]

# Output text
outcome = f"""Election Results\n
-------------------------\n
Total Votes: {total_votes}\n
-------------------------\n
"""

for candidate in candidates_votes:
        votes = candidates_votes[candidate]["votes"]
        percentage = candidates_votes[candidate]["percentage"]
        outcome += f'{candidate}: {percentage}%  ({votes})\n \n'

outcome += f"""
-------------------------\n
Winner: {max_candidate[0]}\n
-------------------------\n
"""
print(outcome)

# Specify the file to write to
output_path = os.path.join( "analysis", "analysis.txt")

# Open the file using "write" mode.
with open(output_path, 'w') as txtfile:
    txtfile.write(outcome)

print("Analysis results have been saved to analysis.txt.")


        

