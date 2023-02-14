#ask the user to enter their weight in kg
weight = int(input("Enter your weight in kg: "))
#ask the user to enter their height in m
height = float(input("Wnnter your height in m: "))

#caluculate the height and the weight given in order to find the BMI
bmi = weight / ((height) * (height))
print(bmi)

#finding out where the users BMI belongs
if bmi >= 30:
    print("Obese")
elif bmi >=25:
    print("Overweight")
elif bmi >=18.5:
    print("Normal")
else:
    print("Underweight")