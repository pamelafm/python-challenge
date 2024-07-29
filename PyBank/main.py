import os
import csv
from pathlib import Path

# Define the path to the CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
previous_profit = None
total_change = 0
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Read the CSV file
with open(csvpath, mode='r') as csvfile:
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        date = row['Date']
        profit_loss = int(row['Profit/Losses'])
        
        # Update the total number of months and net total
        total_months += 1
        net_total += profit_loss
        
        # Calculate the change in profit/losses
        if previous_profit is not None:
            change = profit_loss - previous_profit
            total_change += change
            
            # Check for the greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase = {"date": date, "amount": change}
            if change < greatest_decrease["amount"]:
                greatest_decrease = {"date": date, "amount": change}
        
        # Update previous profit/loss
        previous_profit = profit_loss

# Calculate average change
average_change = total_change / (total_months - 1) if total_months > 1 else 0

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Write results to a text file
output_path = Path('financial_analysis.txt')
with output_path.open(mode='w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")