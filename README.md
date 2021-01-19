# Election_Analysis

## Overview of Election Audit
To complete the analysis of election results for the Colorado Board of Elections. 

The overall objective is to go through the election results and calculate a few metrics and write the output to the file. The metrics to be calculated are:
1. Calculating the total votes cast
2. Identifying the list of candidates for whom votes have been cast
3. Calculating the total number of votes each candidate received
4. Calculating the percentage of votes each candidate received
5. Determining the winner of the election based on popular vote

## Resources
- Data source: Election_results.csv
- Software: Python 3.8.5, Visual Studio Code

## Summary

### Election Audit Results
The analysis of the results is as follows:

#### The output as seen in the terminal window

![Election Analysis Summary](https://github.com/dkatragadda/Election_Analysis/blob/main/Resources/Election_Results_Screenshot.png)

#### The output as seen in the elections_results txt file in the Analysis folder
![Election_Results_Text](https://github.com/dkatragadda/Election_Analysis/blob/main/Resources/Election_Results_text_Screenshot.png)

### Election Audit Summary
This analysis uses the dataset 'Elections_results.csv'. We have utilized two packages 'os' and 'csv' to perform operations on the dataset. Using the for loop counters as we read through each row of the file, we have analysed the results and calculated the winner of the election and also sliced the data by the different counties in which the voting occured. Note that the output of the analysis can be altered by changing the dataset in the csv file. 

The script can be modified to display the output in a different format if required by the board. For ex: the sequence in which the output is printed in the file can be altered. Another change that can be made to the script would be to calculate the voter turnout by candidate in each county to determine where the candidates are receiving their votes. 
