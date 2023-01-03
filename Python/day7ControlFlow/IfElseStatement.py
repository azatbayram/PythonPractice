#If else statement
score=60

if(score>=70):
    print("Excellent")
    print("You passed with grade A")
else:
    print("You failed")

sales=4000
salary=1000

if(sales>=5000):
    bonus=500
    commissionRate=1.12
else:
    bonus=100
    commissionRate=1.1

salary=salary*commissionRate+bonus
text="Your salary is {} $"
print(text.format(salary))