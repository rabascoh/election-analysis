import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total vote counter
total_votes = 0

#declare candidate option list
candidate_options = []

#declare candidate votes dictionary
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze data here. 

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Count the total votes.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        #get candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Start counting candidate's votes
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        #initialize winning candidate
        winning_candidate = ""
        #declare winning count
        winning_count = 0
        #declare winning percentage
        winning_percentage = 0

        # Iterate through the candidate list.
        for candidate_name in candidate_votes:
                # Retrieve vote count of a candidate.
                votes = candidate_votes[candidate_name]
                # Calculate the percentage of votes.
                vote_percentage = float(votes) / float(total_votes) * 100
                #Determine winning vote count and candidate

                #print candidate's name, vote count and percentage
                candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
                
                #  Save the candidate results to our text file.
                txt_file.write(candidate_results)

                #Determine if the votes are greater than the winning count.
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                    # If true then set winning_count = votes and winning_percent =
                    # vote_percentage.
                    winning_count = votes
                    winning_percentage = vote_percentage
                    # Set the winning_candidate equal to the candidate's name.
                    winning_candidate = candidate_name
                    winning_candidate_summary = (
                        f"-------------------------\n"
                        f"Winner: {winning_candidate}\n"
                        f"Winning Vote Count: {winning_count:,}\n"
                        f"Winning Percentage: {winning_percentage:.1f}%\n"
                        f"-------------------------\n")
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)
