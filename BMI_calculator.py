print("Hello , you are welcome to the BMI calculator!")


def ask_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number :)")
            else:
                return value
        except ValueError:
            print("Please enter a valid number")


height = ask_float("Enter your height in meter: ")
weight = ask_float("Enter your weight in kilos: ")
BMI = (float(weight) / float(height) ** 2)
print(f"Your BMI is: {round(BMI, 2)}!")
if BMI < 18.5:
    print("You are underweight.")
elif BMI < 25:
    print("You have a normal weight.")
elif BMI < 30:
    print("You are overweight.")
else:
    print("You are obese.")