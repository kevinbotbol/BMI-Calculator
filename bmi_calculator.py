weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

if weight <= 0 or height <= 0:
    print("Error: Weight and height must be greater than zero.")
else:
    bmi = weight / (height * height)

    print("Your BMI is:", bmi)

    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi < 25:
        print("Category: Normal weight")
    elif bmi < 30:
        print("Category: Overweight")
    else:
        print("Category: Obese")
