import os
import csv

# Find csv file in resources folder
filepath = os.path.join('Resources', 'election_data.csv')

cand_names = []
perc_cands_won = []
cands_votes = []

total_votes = 0
greatest_votes = 0

# Open in the CSV file
with open(filepath, 'r') as csvfile:

    # Read and split the data on commas
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csv_reader)
    # print(f"CSV Header: {csv_header}") no need to print
    
    # Read each row afterheader and create new lists for each candidate and their no. of votes
    for row in csv_reader:
        # asign candidate variable to the name in the line 
        candidate = row[2]
        total_votes = total_votes + 1
        
        # check if this name is already in the appended list of cand names
        if candidate in cand_names:
            # if it is in the list keep track of no of candidates (for indexing)
            candidate_no = cand_names.index(candidate) # returns the location of name in the list of candidates for indexing other lists
            # match and tally votes to each candidate using index found above
            cands_votes[candidate_no] = cands_votes[candidate_no] + 1
        # if not in the list of candidate names then add the new name to the list and assign new name with 1 vote
        else: # the first line of each new candidate will come here because there is nothing in the list yet about that candidate
            cand_names.append(candidate)
            cands_votes.append(1)
    
    # Calculate the % of votes won by each candidate and make a new list and determine winner
    for row in range(len(cands_votes)):
        perc = round(((cands_votes[row])/total_votes * 100),3)
        perc_cands_won.append(perc)
        # determine winner
        if row > greatest_votes:
            greatest_votes = cands_votes[row]
            name_winner = cand_names[row]

#print(f"{csv_header}")
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------")

for row in range(len(cands_votes)):
    print(f"{cand_names[row]}: {perc_cands_won[row]}% ({cands_votes[row]})")

print("----------------------------")
print(f"Winner: {name_winner}")
print("----------------------------")

# Create path and write the results of analysis to a new text file
data_output = os.path.join('analysis', 'data_analysis2_results.txt')

with open(data_output, 'w') as datafile:

    datafile.write('Election Results\n')
    datafile.write('----------------------------\n')
    datafile.write('Total Votes: ' + str(total_votes) + '\n')
    datafile.write('----------------------------\n')

    for row in range(len(cands_votes)):
        datafile.write(f'{cand_names[row]}: {perc_cands_won[row]}% ({cands_votes[row]})\n')

    datafile.write('----------------------------\n')
    datafile.write(f'Winner: {name_winner}\n')
    datafile.write('----------------------------\n')
