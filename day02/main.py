print("Welcome to the Tip Calculator!")
bill = int(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + tip / 100)
bill_each_person = bill_with_tip / people

print(f"Each person should pay: ${bill_each_person:.2f}")
