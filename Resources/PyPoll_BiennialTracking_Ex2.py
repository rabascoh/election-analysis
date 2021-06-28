# Add dependencies.
import csv
import os

# Assign a variable for the file to load and the path (updated new file & path).
file_to_load = os.path.join("ex2_election_results.csv")

# Assign a variable to to save the file to a path.
file_to_save = os.path.join("ex2_election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# ADD YEAR
year = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_list = []
county_votes = {}

# CREATE A YEAR LIST AND YEAR VOTES DIRECTORY
year_list = []
year_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
county_turnout = 0

# TRACK HIGHEST VOTER TURNOUT FOR YEAR AND YEARLY VOTER TURNOUT
highest_year = 0
year_turnout = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header
    header = next(file_reader)

    # For each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        #Get the year from each row.
        year = row[3]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that county's vote count.
        county_votes[county_name] += 1

        # Write an if statement that checks that the
        # year does not match any existing years in the year list.
        if year not in year_list:

            # Add the existing year to the list of years.
            year_list.append(year)

            # Begin tracking the year's vote count.
            year_votes[year] = 0

        # Add a vote to that year's vote count.
        year_votes[year] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        county_vote_count = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = float(county_vote_count) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
        f"{county_name}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")

        print(county_results)
        
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_vote_count > county_turnout):
            largest_county = county_name
            county_turnout = county_vote_count

    # 7: Print the county with the largest turnout to the terminal.
    largest_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")

    print(largest_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_summary)

    ##ADDED YEAR ANALYSIS
    # Write a for loop to get the year from the year dictionary.
    for year in year_votes:
        # Retrieve the year vote count.
        year_vote_count = year_votes.get(year)
        # Calculate the percentage of votes for that year.
        year_vote_percentage = float(year_vote_count) / float(total_votes) * 100

         # Print the year results to the terminal.
        year_results = (
        f"{year}: {year_vote_percentage:.1f}% ({year_vote_count:,})\n")

        print(year_results)
        
         # Save the year votes to a text file.
        txt_file.write(year_results)

         # Write an if statement to determine the winning year and get its vote count.
        if (year_vote_count > year_turnout):
            highest_year = year
            year_turnout = year_vote_count

    # Print the county with the largest turnout to the terminal.
    highest_year_summary = (
        f"-------------------------\n"
        f"Year with the Highest Turnout: {highest_year}\n"
        f"-------------------------\n")

    print(highest_year_summary)

    # Save the county with the largest turnout to a text file.
    txt_file.write(highest_year_summary)

    # Save the final candidate vote count to the text file.
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

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
