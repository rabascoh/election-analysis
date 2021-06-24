#elections analysis for CO counties

#conditionals example
counties = ["Arapahoe","Denver","Jefferson"]
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#list for loop example
for i in range(len(counties)):
    print(counties[i])

#tuple for loop example
counties_tuple = ("Arapahoe","Denver","Jefferson")

for i in range(len(counties_tuple)):
    print(counties_tuple[i])


#dictionary example
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#keys specified example
for county in counties_dict.keys():
     print(county)

#get the number of voters per county
for voters in counties_dict.values():
    print(voters)

#get the number of voters using county key
for county in counties_dict:
    print(counties_dict[county])

#get the number of voters using 'get'
for county in counties_dict:
     print(counties_dict.get(county))

#get key & value pairs for counties' voter data
for key, value in counties_dict.items():
    print(key, "county has", value, "registered voters. ")

#printing each dict in voting data
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                 {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#retrieve values for each dictionary
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#f string example
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")

#multi-line f string
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)