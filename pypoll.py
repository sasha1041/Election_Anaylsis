import csv
import os
from time import sleep

CSV_PATH = "Resources/election_results.csv"
COUNTY_INDEX = 1

# my help with file note found error in vs code
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# How to open file
with open(CSV_PATH) as csv_file:
    print(type(csv_file))
    reader = csv.reader(csv_file)
    for row in reader:
        print(type(row))
        #printing each row in the index
        print(row)

print(row[COUNTY_INDEX])




# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")
# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

# More conscise 

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Counties in Election")
    txt_file.write("Arapahoe\nDenver\nJefferson")

# \n is to add a new line between each string. Can also insert commas and spaces
# to reflect a list


# Read the file object with the reader function.
file_reader = csv.reader(election_results)

# Print each row in the CSV file.
for row in file_reader:
    print(row)



# # Read the file object with the reader function.
# file_reader = csv.reader(election_analysis)

#     # Print the header row.
# headers = next(file_reader)
#     print(headers)

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_results:
    file_reader = csv.reader(election_results)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# (left off on 3.4