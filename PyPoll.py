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

# Opening the csv file
with open(file_to_load,'r') as election_data:
    
    # To do: perform analysis
    file_reader=csv.reader(election_data,delimiter=',')

    # Print header row in csv file
    file_header = next(file_reader)
    print(file_header)


    # for row in file_reader:
    #     print(row)
    

# Creating a file path to write the output
file_to_write = os.path.join('Analysis','election_analysis.txt')
with open(file_to_write,'w') as election_output:
    election_output.write('Counties in the election\n')
    election_output.write('------------------------\n')
    election_output.write('Arapahoe\n')
    election_output.write('Denver\n')
    election_output.write('Jefferson\n')

election_output.close()

