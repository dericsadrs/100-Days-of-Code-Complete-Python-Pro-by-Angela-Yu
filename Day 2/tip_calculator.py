#
# Created on Wed May 31 2023
# Created by Software Engineer Deric San Andres
#

print("Welcome to the Tip Calculator: ")
bill = float(input("What was the total bill?: "))
tip = int(input("How much tip would you like to give 10, 12, or 15?: "))
people = int(input("How many people to split the bill: "))
tip_percent = tip / 100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)
print(f"Each person should pay ${final_amount}")
if bill > 0:
    if tip == 10 or tip == 12 or tip == 15:
        pass

