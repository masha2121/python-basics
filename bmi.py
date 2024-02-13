height = float(input("enter your height in metres"))
weight = float(input("enter your weight in kg"))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("below average")
elif bmi >= 18.5 and bmi < 25:
    print("average")
else:
    print("above average")


