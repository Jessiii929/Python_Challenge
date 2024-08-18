import os
import csv

#Path to election data from the resources folder
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
#Total votes calculation and total votes per candidate
    total_votes=0

    candidates = {"Charles Casper Stockham":0, "Diana DeGette":0, "Raymon Anthony Doane":0}
    for row in csvreader:
        total_votes+=1
        
        candidate_name = row[2]
        candidates[candidate_name]=candidates[candidate_name]+1
    
#Percentage calculation for each candidate
    for candidate,vote_count in candidates.items():
        percentage = (vote_count/total_votes)*100
        candidates[candidate]=percentage
    
    for candidate, percentage in candidates.items():
        print(f"{candidate}: {percentage:.3f}%")

#Winner based on popular vote
    winner = max(candidates, key=candidates.get)


analysis_results = "analysis/results.txt"

output="Election Results\n"
output+="-----------------------\n"
output+=f"Total Votes: {total_votes}\n"
output+="-----------------------\n"
output+=f"{candidate}: {percentage:.3f}%:\n"
output+="-----------------------\n"
output+=f"Winner: {winner}\n"
output+="-----------------------"
print(output)

with open(analysis_results,"w") as text_file:
    text_file.write(output)  