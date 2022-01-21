import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join("/Users/lisahanson/desktop/Resources_3", "/Users/lisahanson/desktop/Resources_3/election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("/Users/lisahanson/desktop/election_analysis/analysis","/Users/lisahanson/desktop/resources_3/election_analysis.txt")

#Open the election results and read the file 
with open(file_to_load) as election_data: 
    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)
    #Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
#Read the file object with the reader function
    #Print the header row
    headers = next(file_reader)
    print(headers)
        
        