# Election Data Analysis
# Open the dataset
# Calculate the total number of votes cast
# Compile list of candidates who received votes
# Calculate total number of votes received by each candidate
# Percentage of votes each candidate won
# Determine the winner of the election based on popular vote

# Importing packages to help with file handling such as OS and CSV
import os
import csv

# Setting the path for the dataset to be read
file_to_load = os.path.join('Resources','election_results.csv')

# Creating a file path to write the output
file_to_save = os.path.join('Analysis','election_analysis.txt')

# Initializing a counter for the votes
total_votes = 0

# Declaring a list to hold the candidates
candidate_options=[]

# Declaring a dictionary to hold the candidate votes
candidate_votes={}

#Declaring winning candidate, winning count and winning percentage
winning_candidate=''
winning_count=0
winning_percentage=0


# Opening the csv file
with open(file_to_load,'r') as election_data:
    
    # To do: perform analysis
    file_reader=csv.reader(election_data,delimiter=',')

    # Read header row in csv file
    file_header = next(file_reader)
    
    # Print each row in csv file
    for row in file_reader:
        # Add total votes count
        total_votes += 1

        # Print the candidate name on each row
        candidate_name = row[2]

        #Add the candidate name to the list
        if candidate_name not in candidate_options:
            # Append the name if it is already not present in the list
            candidate_options.append(candidate_name)

            # Being tracking the candidate vote count
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1
        
# Determine the vote percentage for each candidate
# 1. Iterate through the candidate list
for candidate_name in candidate_votes:
    # 2. Retrieve vote count for each candidate
    votes=candidate_votes[candidate_name]
    # 3. Calculate vote percentage
    vote_percentage = float(votes)/float(total_votes) * 100
    # 4. Print the candidate name and the vote percentage
    print(f'{candidate_name}: received {vote_percentage:.1f}%  ({votes}) \n') 

    # Determine winning vote count and candidate
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        # If true set the votes as the winning count and the winning percentage
        winning_count=votes
        winning_percentage=vote_percentage
        # Set the name of the winning candidate
        winning_candidate = candidate_name

# Print out the winning candidate
winning_candidate_summary = (
    f'----------------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning vote count: {winning_count}\n'
    f'Winning vote percentage: {winning_percentage:.1f}\n'
    f'----------------------------------\n')
print(winning_candidate_summary)
# print(f'The winning candidate is {winning_candidate} and received {winning_count} votes with {winning_percentage:.1f}% of the vote')
    
with open(file_to_save,'w') as election_output:
    election_output.write('Counties in the election\n')
    election_output.write('------------------------\n')
    election_output.write('Arapahoe\n')
    election_output.write('Denver\n')
    election_output.write('Jefferson\n')


election_data.close()
election_output.close()


