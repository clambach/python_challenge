import os
import csv
 
#Variables and lists to store data
count = []
change = []
unique = []
candidates = []

#Pull the csv file
csvpath = 'Instructions-4/PyPoll/Resources/election_data.csv'

#open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #store data from rows
    for row in csvreader:
     count.append(row[0])
     unique.append(row[2])
    candidates = [*set(unique)]

    #print queries
    print(" ")
    print("Election Results")
    print("--------------------- ")
    print(f"Total Votes:  {len(count)}")
    print("--------------------- ")
    print("Candidates:")
    for x in candidates:
       print(x)

 

 #create text file with outcomes
    outputpoll = os.path.join('.','outputpoll.txt')
    with open(outputpoll,"w") as new:
       new.write("Election Results")
       new.write("\n")
       new.write("------------------- ")
       new.write("\n")
       new.write(f"Total Votes:  {len(count)}")
       new.write(x)
