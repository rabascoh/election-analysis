# Election Analysis

## Overview of Election Audit
The purpose of this project is to perform an election audit of a local congressional election in Colorado. The two key ojectives are to determine the winner of the election (based on popular vote) and determine the county with the largest voter turnout. 

## Election Audit Results: 
- Total Votes:
	- There were 369,711 votes cast in the election. 
- County Votes: 
	- Denver residents cast 306,055 votes and 82.8% of the total votes. 
	- Jefferson residents cast 38,855 votes and 10.5% of the total votes. 
	- Arapahoe residents cast 24,801 votes and 6.7% of the total votes. 
- Largest County Turnout: 
	- The county with the largest number of votes was Denver with 306,055 votes and 82.8% of the total votes. 
- Candidate Results: 
	- Diana DeGette received 272,892 votes and 73.8% of total votes. 
	- Charles Casper Stockham received 85,213 votes and 23.0% of the total votes. 
	- Raymon Anthony Doane received 11,606 votes and 3.1% of the total votes. 
- Winner of the Election: 
	- Diana DeGette won the election with 272,892 votes and 73.8% of the total votes.

## Election Audit Summary: 
This election audit analysis can be replicated for any election with some modifications. 
### Local Election Audit
To report on local election data without several counties, remove (or "comment out") the county level analysis and only report on the candidate votes and winning candidate. The following analysis has been updated for local elections. 

[Local Election Audit](https://github.com/rabascoh/election-analysis/blob/main/Resources/PyPoll_LocalElections_Ex1.py)

Please see the Election Audit results updated to the Local Election format below. 

[Local Election Results Format](https://github.com/rabascoh/election-analysis/blob/main/Resources/ex1_election_analysis.txt)

### Biennial Congressional Election Audit
To track election results over time, add a field for the year and append the data for the previous years' election data to the election results file. 
[ADD REC]

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.2

