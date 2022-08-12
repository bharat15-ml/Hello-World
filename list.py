expenses=[10,20,30,40,50,60,70,80,90]

def total_expenditure(expenses):
    total=0;
    for i in expenses:
        total=total+i;
    return total;

total=total_expenditure(expenses)
print("total expenses:",total)
