# if statement
score=85

if(score>=70):
    print("Excellent")
    print("You passed with grade A")

sales=5000
salary=1000

if(sales>=5000):
    bonus=500
    commissionRate=1.12
    salary=salary*commissionRate+bonus

text="Your salary is {} $"
print(text.format(salary))