import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# list to store data
change = []

# Read in the CSV file
with open( budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    data = list(csvreader)

    # to calculate the total number of months
    total_months = len(data)

    # to calculate the net total amount of "Profit/Losses" over the entire period
    net_total = sum(int(row[1]) for row in data)

    # list to store data
    changes = []
    last_profit_loss = int(data[0][1])
    
    # to calculate change over each month
    for row in data[1:]:
        current_profit_loss = int(row[1])
        change = current_profit_loss - last_profit_loss
        changes.append(change)
        last_profit_loss = current_profit_loss


    # to calculate avergae change
    average_change = round(sum(changes) / len(changes), 2)

    # to calculate greateest increase in profits
    maximum_change_increase = max(changes)
    max_increase_index = changes.index(maximum_change_increase)
    max_increase_date = data[max_increase_index + 1][0]
    
    
    # to calculate greatest decrease in profits 
    maximum_change_decrease = min(changes)
    max_decrease_index = changes.index(maximum_change_decrease)
    max_decrease_date = data[max_decrease_index + 1][0]

# output text
output = (f"""
Financial Analysis

----------------------------

Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change}
Greatest Increase in Profits: {max_increase_date} (${maximum_change_increase})
Greatest Decrease in Profits: {max_decrease_date} (${maximum_change_decrease})
""")
print(output)

# Specify the file to write to
output_path = os.path.join( "analysis", "analysis.txt")

# Open the file using "write" mode.
with open(output_path, 'w') as txtfile:
    txtfile.write(output)

print("Analysis results have been saved to analysis.txt.")