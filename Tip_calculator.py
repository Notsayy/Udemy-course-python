print("Welcome to the tip calculator!")

def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Please enter a positive number.")

def get_int_choice(prompt, choices):
    while True:
        try:
            value = int(input(prompt))
            if value in choices:
                return value
            else:
                print(f"Please enter one of the following: {choices}")
        except ValueError:
            print(f"Please enter one of the following: {choices}")

def get_int_positive(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value >= 1:
                return value
            else:
                print("Please enter a number of at least 1.")
        except ValueError:
            print("Please enter a number of at least 1.")

total_bill = get_float("What was the total bill? $ ")
tip = get_int_choice("How much tip would you like to give? 10, 12 or 15? ", [10, 12, 15])
splitting_bill = get_int_positive("How many people to split the bill? ")

bill_with_tip = total_bill + (total_bill * tip / 100)
final_bill = bill_with_tip / splitting_bill

print(f"Each person should pay: ${final_bill:.2f}")
