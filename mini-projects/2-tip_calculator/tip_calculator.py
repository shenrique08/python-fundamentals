print("\n------- Welcome to the Tip Calculator ---------\n")

total_bill = float(input("What was the total bill? R$"))
percentage_of_the_bill = float(input("How much tip would you like to give? %"))
amount_of_people = int(input("How many people split the bill? "))

percentage_of_the_bill = percentage_of_the_bill * 0.01
bill_for_each_person = (total_bill + (total_bill * percentage_of_the_bill)) / amount_of_people

print(f"Each person should pay: R${bill_for_each_person}")
