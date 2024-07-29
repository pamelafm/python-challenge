import os
import csv

# Define file paths
csvpath = os.path.join('Resources', 'election_data.csv')
output_file = 'election_results.txt'

def analyze_votes(csvpath):
    # Initialize variables
    total_votes = 0
    candidate_votes = {}

    # Open the CSV file
    with open(csvpath, mode='r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # Read the header row
        csv_header = next(csvreader)
        
        # Process each row in the CSV
        for row in csvreader:
            total_votes += 1
            candidate = row[2]  # Assuming 'Candidate' is the third column
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1
    
    # Determine the winner and calculate percentages
    winner = ""
    max_votes = 0
    results = []

    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        results.append((candidate, votes, percentage))
        if votes > max_votes:
            max_votes = votes
            winner = candidate
    
    # Sort results by number of votes in descending order
    results.sort(key=lambda x: x[1], reverse=True)
    
    # Generate output for terminal and file
    output_lines = []
    output_lines.append("Election Results")
    output_lines.append("-------------------------")
    output_lines.append(f"Total Votes: {total_votes}")
    output_lines.append("-------------------------")
    
    for candidate, votes, percentage in results:
        output_lines.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    output_lines.append("-------------------------")
    output_lines.append(f"Winner: {winner}")
    output_lines.append("-------------------------")
    
    # Print results to terminal
    for line in output_lines:
        print(line)
    
    # Write results to a text file
    with open(output_file, mode='w') as file:
        for line in output_lines:
            file.write(line + '\n')

# Run the analysis
analyze_votes(csvpath)