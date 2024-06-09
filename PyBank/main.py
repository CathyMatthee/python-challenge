import os
import csv

# Find csv file in resources folder
filepath = os.path.join('Resources', 'budget_data.csv')

# List variables to store data
proforloss = []
change_in_proforloss = []
date = []

# Open in the CSV file
with open(filepath) as csvfile:

    # Read and split the data on commas
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csv_reader)
    # print(f"CSV Header: {csv_header}")
    
    # Calculate the no of months
    total = 0
    total_change = 0
    GIncP = 0
    GDecP = 0

    # Read each row afterheader
    for row in csv_reader:
        # Create list to perform calculations on for profit & loss values from a string in row[1] in csv file
        amount = int(row[1])
        proforloss.append(amount)
        total = total + amount
        date.append(row[0])
    
    # Calculate the no of months
    no_months = len(proforloss)

    # change in profit and loss month to month = closing price - opening price
    for i in range(1, len(proforloss)):
        calculate_change = proforloss[i]-proforloss[i-1]
        # Create list for change in profit & loss
        change_in_proforloss.append(calculate_change)

        # calculate the total profit and loss
        total_change = total_change + calculate_change

        # calculate the GIncP and GDecP 
        if change_in_proforloss[i-1] > GIncP:
            GIncP = change_in_proforloss[i-1]
            Inc_date = date[i]
        
        if change_in_proforloss[i-1] < GDecP:
            GDecP = change_in_proforloss[i-1]
            Dec_date = date[i]

    # Calculate average change

    ave_change = round((total_change/(no_months-1)),2)

# Writing a function that returns the average of the gains and losses for a list of number

#print(f"{csv_header}")
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(no_months))
print(f"Total: $" + str(total))
print("Average Change: $" + str(ave_change))
print("Greatest Increase in Profits: " + Inc_date + " (" + str(GIncP) + ")")
print("Greatest Decrease in Profits: " + Dec_date + " (" + str(GDecP) + ")")


#print(average(range(length)))

# Create path and write the results of analysis to a new .csv file
data_output = os.path.join('analysis', 'data_analysis_results.txt')

with open(data_output, 'w') as datafile:

    datafile.write('Financial Analysis\n')
    datafile.write('----------------------------\n')
    datafile.write('Total Months: ' + str(no_months) + '\n')
    datafile.write('Total: $' + str(total) + '\n')
    datafile.write('Average Change: $' + str(ave_change) + '\n')
    datafile.write('Greatest Increase in Profits: ' + Inc_date + " (" + str(GIncP) + ")" + '\n')
    datafile.write('Greatest Decrease in Profits: ' + Dec_date + " (" + str(GDecP) + ")" + '\n')
    
