height = float(input("Enter the height in m: "))
weight = float(input("Enter the weight in kg: "))

bmi = weight / (height * height)

print(f"The BMI is approximately {round(bmi)}")
