# Overview of the Election Audit
  A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 

## The audit of the candidate results included the following steps:
1. Calculating the total number of votes cast.
2. Getting a complete list of candidate who received votes.
3. Calculating the total number of votes each candidate received.
4. Calculating the percentage of votes each candidate won.
5. Determining the winner of the election based on popular vote. 

## The audit of the election results also included outcomes by county: 
1. Adding the voter turnout for each county
2. Getting the percentage of votes from each county out of the total count
3. Getting the county with the highest turnout 

# Election-Audit Results:
## Candidate Results
The analysis of the election by candidate: 
- There were "369,711" votes cast in the election. 
- The candidates were: 
  - Charles Casper Stockham 
  - Diana DeGette 
  - Raymon Anthony Doane 
- The candidate results were:
  - Charles Casper Stockham received "23.0%" of the vote and 85,213 number of votes. 
  - Diana DeGette received "73.8%" of the vote and 272,892 number of votes.
  - Raymond Anthony Doane received "3.1%" of the vote and "11,606" number of votes.
- The winner of the election: 
  - Dianna DeGette who received "73.8%" of the vote and "272,892" number of votes. 
## County Results
The analysis of the election by county:
- There were three counties included in the analysis: 
  - Jefferson, Denver and Arapahoe 
- The voter turnout by county: 
  - Jefferson: 38,855 votes and 10.5% of the vote
  - Denver: 306,055 votes and 82.8% of the vote
  - Arapahoe: 24,801 votes and 6.7% of the vote 
- The county with the largest voter turnout: 
   - Denver, with 306,055 votes and 82.8% overall turnout. 

# Election-Audit Summary: 
This script can easily be run for other elections with similar raw data sets. The below samples of code demonstrate its modularity. There is no specific reference to a county or a candidate, making it very adaptable to other elections. 

## Using lists, dictionaries and variables to collate the data:
### For Candidate Analysis: 
``` candidate_options = []
    county_votes = {} 
    # for tracking the winning canddiate
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0

```
### For County Analysis: 
``` county_list = []
    county_votes = {} 
    # for tracking county and largest turnout
    largest_county = ""
    largest_county_count = 0
    largest_county_percentage = 0
```

## Using for loops to iternate through the data and retrieve name and vote:
### For Candidate Analysis
```
for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
```

### For County Analysis 
```
for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        vote_count = county_votes[county_name]

        # 6c: Calculate the percent of total votes for the county.
        vote_percentage = float(vote_count) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({vote_count:,}) \n")

         # 6d: Print the county results to the terminal.
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

```

## Using decision statements to determine the winning candidate and county with the largest turnout. 

### Decision statement used for the candidate analysis
```
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            print(candidate_name)

```
### Decision statement used for the county analysis
```
        6f: Write a decision statement to determine the winning county and get its vote count.
        if (vote_count > winning_count) and (vote_percentage > winning_percentage):
            winning_count = vote_count
            winning_county = county_name
            winning_percentage = vote_percentage
```
