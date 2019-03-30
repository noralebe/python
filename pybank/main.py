import csv
#file = "../Python Stuff/budget_data.csv"
months = 0
rows = []
profitslosses = 0
greatestincrease = 0
greatestincrease_date = 0
greatestdecrease = 0
greatestdecrease_date = 0
variance=0
newcolumn=[]
with open("budget_data.csv", "r") as csvfile:
    csvreader = csv.reader (csvfile, delimiter=",")
    header = next(csvreader)
    first_row = next(csvreader)
    previousprofitloss = float(first_row[1])
    months = months + 1
    for row in csvreader:
        months = months + 1
        profitslosses = profitslosses + float(row [1])
        variance = float(row[1])-previousprofitloss
        newcolumn = newcolumn + [variance]
        previousprofitloss = float(row[1])
        if float (row[1])> greatestincrease:
            greatestincrease=float(row[1])
            greatestincrease_date= row[0]
        if float (row[1])< greatestdecrease:
            greatestdecrease=float(row[1])
            greatestdecrease_date= row[0]
       
      
    print(f"Financial Analysis")
    print(f'----------------------')
    print(f"Total Months: {months}")
    print(f"Total: ${profitslosses}")
    print(f"Average Change: ${round((sum(newcolumn)/(months-1)),2)}")
    print(f"Greatest Increase in Profits: {greatestincrease_date} (${greatestincrease})")
    print(f"Greatest Decrease in Profits: {greatestdecrease_date} (${greatestdecrease})")

    mybank=open("outputfile.txt", 'w+')
    mybank.write(f"Total months: {months}\n")
    mybank.write(f"Total: ${profitslosses}\n")
    mybank.write(f"Average Change: ${round((sum(newcolumn)/(months-1)),2)}\n")
    mybank.write(f"Greatest Increase in Profits: {greatestincrease_date} (${greatestincrease})\n")
    mybank.write(f"Greatest Decrease in Profits: {greatestdecrease_date} (${greatestdecrease})\n")
    mybank.close()
  


    
   