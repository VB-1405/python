weight = int(input("Enter your weight in kg: "))
heightin = float(input("Enter your height in metre: "))

height = heightin * heightin

bmi = weight/height

if bmi < 18.5:
    print("Underweight")

elif bmi > 18.5 and bmi < 25:
    print("Normal")

elif bmi >= 25 and bmi < 30:
    print("Overweight")

elif bmi >= 30: 
    print("Obesity")    
