#import modules
import os
import csv

# path to collect PyBank Budget data
budget_data_csv = os.path.join('..', 'PyBank_Resources', 'budget_data.csv')
# Set an output path for the text file .txt
text_path = "output.txt"

# now improve the reading using the csv module

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
greatest_profit_decrease = ["", 0]
greatest_profit_increase = ["", 0]
profit_change_list = []
profit_avg = 0
data = []
# The net total amount of "Profit/Losses" over the entire period
with open(budget_data_csv) as csvfile:
    csvreader = csv.DictReader(csvfile)
    #loop through to find the total months
    for row in csvreader:
        #count the total months
        # total_months += 1
        # #calculate the total profit over the entire period
        # total_profit = total_profit + int(row["Profit/Losses"])
        # # average of the changes in "Profit/Losses" over the entire period
        # profit_change = float(row["Profit/Losses"]) - previous_profit
        # previous_profit = float(row["Profit/Losses"])
        # profit_change_list.append(profit_change)
        # month_of_change.append(row["Date"])
        data.append([row["Date"],int(row["Profit/Losses"])])
    print(data)
    

    max_rows=len(data)
    for item in data:
        total_profit = total_profit + item[1]
    for i in range(1, max_rows):
        profit_change = data[i][1] - data[i-1][1]
        month_of_change.append(profit_change)
        if profit_change > greatest_profit_increase[1]:
            greatest_profit_increase[1] = profit_change
            greatest_profit_increase[0] = data[i][0]
        if profit_change < greatest_profit_decrease[1]:
            greatest_profit_decrease[1] = profit_change
            greatest_profit_decrease[0] = data[i][0]

    profit_avg = sum(month_of_change)/len(month_of_change)
    print("Profit Average: ", profit_avg)
    print("Greatest Increase: ", greatest_profit_increase[0], "  ", greatest_profit_increase[1])
    print("Greatest Decrease: ", greatest_profit_decrease[0], "  ", greatest_profit_decrease[1])
    
    
#     profit_avg = sum(profit_change_list[1:])/len(profit_change_list[1:])
    
#         # Greatest increase in profits (date and amount) over the entire period
#     maximum_profit = max(profit_change_list)
#     month_index = profit_change_list.index(maximum_profit)
#     maximum_month = month_of_change[month_index]
    

#         # Greatest decrease in profits (date and amount) over the entire period
#     minimum_profit = min(profit_change_list)
#     month_index = profit_change_list.index(minimum_profit)
#     minimum_month = month_of_change[month_index]
    
# #Print the summnary of my financial analysis...

# print("Financial Analysis")
# print("_________________________")
# print(f"Total Months: {total_months}")
# print(f"Total: ${total_profit}")
# print(f"Average Change: ${profit_avg}")
# print(f"Greatest Increase in Profits: {maximum_month} (${maximum_profit})")
# print(f"Greatest Decrease in Profits: {minimum_month} (${minimum_profit})")

# # Export a text file with the results...
# text_path = "output.txt"
# saved_file = budget_data_csv.strip(".csv") + text_path
# file_path = os.path.join(".", saved_file)
# with open(file_path, "w") as text:
#     text.write("Financial Analysis/n")
#     text.write("_________________________/n")
#     text.write(f"Total Months: {total_months}/n")
#     text.write(f"Total: ${total_profit}/n")
#     text.write(f"Average Change: ${profit_avg}/n")
#     text.write(f"Greatest Increase in Profits: {maximum_month} (${maximum_profit})/n")
#     text.write(f"Greatest Decrease in Profits: {minimum_month} (${minimum_profit})/n")

