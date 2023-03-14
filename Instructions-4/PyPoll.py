import os
import csv
 
#Variables and lists to store data
total = 0
count = []
per = []
change = []
unique = []
candidates = []

#Pull the csv file
csvpath = 'PyPoll/Resources/election_data.csv'

#open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #store data from rows
    for row in csvreader:
     count.append(row[0])
     unique.append(row[2])
    candidates = [*set(unique)]
    # per.append(sum(row[2])/count)

from collections import Counter
 
def winner(input):
 
    # convert list of candidates into dictionary
    # output will be likes candidates = {'A':2, 'B':4}
    votes = Counter(input)
     
    # create another dictionary and it's key will
    # be count of votes values will be name of
    # candidates
    dict = {}
 
    for value in votes.values():
 
        # initialize empty list to each key to
        # insert candidate names having same
        # number of votes
        dict[value] = []
 
    for (key,value) in votes.items():
        dict[value].append(key)
 
    # sort keys in descending order to get maximum
    # value of votes
    maxVote = sorted(dict.keys(),reverse=True)[0]
 
    # check if more than 1 candidates have same
    # number of votes. If yes, then sort the list
    # first and print first element
    if len(dict[maxVote])>1:
        print (sorted(dict[maxVote])[0])
    else:
        print (dict[maxVote][0])
 
# Driver program
if __name__ == "__main__":
    input =['john','johnny','jackie','johnny',
            'john','jackie','jamie','jamie',
            'john','johnny','jamie','johnny',
            'john']
    winner(input)



    
    #  loss.append(int(row[1]))

    #  #total votes
    # for i in range(len(loss)-1):
    #     change.append(loss[i-1]-loss[i])


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
       new.write("\n")
       new.write(f"")
       new.write("\n")
       new.write(f"")
       new.write("\n")
       new.write(f"")
       new.write("\n")
       new.write(f"")