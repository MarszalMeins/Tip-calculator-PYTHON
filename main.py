print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100 + 1
amount_of_people = int(input("How many people to split the bill? "))

payment = round((total_bill * tip_percentage) / amount_of_people, 2)
print(f"Each person should pay: ${payment}")