import os
import csv

#Variables and lists to store data
total = 0
count = []
loss = []
change = []
change1 = []

#Pull the csv file
csvpath = 'Instructions-4/PyBank/Resources/budget_data.csv'

#open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #store headers
    csv_header = next(csvreader)

    firstrow = next(csvreader)
    top = firstrow[1]


    #store data from rows
    for row in csvreader:
       count.append(row[0])
       loss.append(int(row[1]))
       change1.append(int(row[1])-int(top))
       top = row[1]

    # #total months
    for i in range(len(loss)):
        change.append(loss[i]-loss[i-1])
    

    #find changes in totals
    increase = change.index(max(change))
    decrease = change.index(min(change))

    #find greatest increase and decrease
    maxincrease = max(change)
    mindecrease = min(change)

    #print queries
    print(" ")
    print("Financial Analysis")
    print("------------------- ")
    print(f"Total Months:  {len(count)+1}")
    print(f"Total:  ${sum(loss)}")
    print(f"Average changes:  {round(sum(change1)/len(change1))}")
    print(f"Best increase:  {count[increase]}  (${(str(maxincrease))})")
    print(f"Worst decrease:  {count[decrease]}  (${(str(mindecrease))})")
    
    #create text file with outcomes
    outputbank = os.path.join('.','outputbank.txt')
    with open(outputbank,"w") as new:
       new.write("Financial Analysis")
       new.write("\n")
       new.write("------------------- ")
       new.write("\n")
       new.write(f"Total Months:  {len(count)+1}")
       new.write("\n")
       new.write(f"Total:  ${sum(loss)}")
       new.write("\n")
       new.write(f"Average changes:  {round(sum(change1)/len((change1)))}")
       new.write("\n")
       new.write(f"Best increase:  {count[increase]}  (${(str(maxincrease))})")
       new.write("\n")
       new.write(f"Worst decrease:  {count[decrease]}  (${(str(mindecrease))})")
