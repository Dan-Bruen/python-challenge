#import modules
import os
import csv

# path to collect PyBank Budget data
budget_data_csv = os.path.join('.', 'Resources', 'budget_data.csv')
# Set an output path for the text file .txt
text_path = "output.txt"

# now improve the reading using the csv module
csv

with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    

#The total number of months included in the dataset
# First I need to set variables:
total_months = 0
total_profit = 0
profit = []
previous_profit = 0
month_of_change = []
profit_change = 0
greatest_profit_decrease = ["", 9999999]
greatest_profit_increase = ["", 0]
profit_change_list = []
profit_avg = 0

# The net total amount of "Profit/Losses" over the entire period
with open(budget_data_csv) as csvfile:
    csvreader = csv.DictReader(csvfile)
    #loop through to find the total months
    for row in csvreader:
        #count the total months
        total_months += 1
        #calculate the total profit over the entire period
        total_profit = total_profit + int(row["Profit/Losses"])
        # average of the changes in "Profit/Losses" over the entire period
        profit_change = float(row["Profit/Losses"]) - previous_profit
        previous_profit = float(row["Profit/Losses"])
        profit_change_list = profit_change_list + [profit_change]
        month_of_change = [month_of_change] [row["Date"]]
        
        # Greatest increase in profits (date and amount) over the entire period
        if profit_change>greatest_profit_increase[1]:
            greatest_profit_increase[1] = profit_change
            greatest_profit_increase[0] = row["Date"]

        # Greatest decrease in profits (date and amount) over the entire period
        if profit_change<greatest_profit_decrease[1]:
            greatest_profit_decrease[1] = profit_change
            greatest_profit_decrease[0] = row["Date"]

    profit_avg = [sum(profit_change)/len(profit_change_list)]

    print(profit_avg)
