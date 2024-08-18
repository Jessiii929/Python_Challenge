import os
import csv

#Path to budget data from the resources folder
csvpath = os.path.join('.','Resources', 'budget_data.csv')
profit_losses=[]
data=[]
#Read in the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    header = next(csvreader)

    for row in csvreader:
        profit_losses.append(int(row[1]))
        data.append((row[0],int(row[1])))

#start and end dates
from datetime import datetime
start_date_str='2010-01'
end_date_str='2017-02'

#converting the date strings to date time objects
start_date=datetime.strptime(start_date_str,'%Y-%m')
end_date=datetime.strptime(end_date_str,'%Y-%m')

#calculating the number of months
total_months=(end_date.year-start_date.year)*12+(end_date.month-start_date.month)+1

#Total amount
net_total=sum(profit_losses)

#Changes in profit/losses over the entire period
changes=[profit_losses[i+1]-profit_losses[i]for i in range(len(profit_losses)-1)]

#Average change calculation
average_change=sum(changes)/len(changes)

#Greatest increase in profits
max_increase=float("-inf")
max_date=""

for i in range(1,len(data)):
    prev_profit=data[i-1][1]
    current_profit=data[i][1]
    increase=current_profit-prev_profit

    if increase>max_increase:
        max_increase=increase
        max_date=data[i][0]

#Greatests decrease in profits
min_decrease=float("inf")
min_date=""

for i in range(1,len(data)):
    prev_profit=data[i-1][1]
    current_profit=data[i][1]
    decrease=current_profit-prev_profit

    if decrease<min_decrease:
        min_decrease=decrease
        min_date=data[i][0]


analysis_results = "analysis/results.txt"

output="Financial Analysis\n"
output+="---------------------------\n"
output+=f"Total Months:{total_months}\n"
output+=f"Total: ${net_total}\n"
output+=f"Average Change: ${average_change:.2f}\n"
output+=f"Greatest Increase in profits:{max_date} (${max_increase})\n"
output+=f"Greatest Decrease in profits:{min_date} (${min_decrease})"
print (output)


with open(analysis_results,"w") as text_file:
    text_file.write(output)      



