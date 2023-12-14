"""
1.Start Program
2. Display Choice: 
    Print "Choose 'investment' or 'bond' to proceed."
3. Get User Input: 
    Input choice (investment/bond)
4. If Choice is 'investment':
    Input deposit amount
    Input interest rate
    Input number of years
    Input interest type (simple/compound)
    If Interest Type is 'simple':
        Calculate simple interest
    Else If Interest Type is 'compound':
        Calculate compound interest
    Display the result
5. Else If Choice is 'bond':
    Input house value
    Input interest rate
    Input number of months for repayment
    Calculate bond repayment
    Display the result
6. End Program
"""

# Function to prompt for a float value
def get_float_input(prompt_message):
    while True:
        try:
            return float(input(prompt_message))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

# Start of the program
print("Choose 'investment' or 'bond' from the menu below to proceed:")
print("investment   - to calculate the amount of interest you'll earn on investment")
print("bond         - to calculate the amount you'll have to pay on a home loan")

# Get the choice from the user with validation
choice = ""
while choice not in ["investment", "bond"]:
    choice = input("Enter your choice (investment/bond): ").lower()
    if choice not in ["investment", "bond"]:
        print("Invalid choice. Please enter 'investment' or 'bond'.")

# Process 'investment' choice
if choice == "investment":
    deposit = get_float_input("Enter the amount you are depositing: ")
    interest_rate = get_float_input("Enter the interest rate (as a percentage): ") / 100
    years = get_float_input("Enter the number of years you plan on investing for: ")
    interest_type = ""
    
    while interest_type not in ["simple", "compound"]:
        interest_type = input("Enter the type of interest (simple/compound): ").lower()
        if interest_type not in ["simple", "compound"]:
            print("Invalid interest type. Please enter 'simple' or 'compound'.")

    if interest_type == "simple":
        total = deposit * (1 + interest_rate * years)
        print(f"The total investment value after {years} years is: {total}")
    else:
        total = deposit * ((1 + interest_rate) ** years)
        print(f"The total investment value after {years} years is: {total}")

# Process 'bond' choice
elif choice == "bond":
    house_value = get_float_input("Enter the present value of the house: ")
    interest_rate = get_float_input("Enter the interest rate (as a percentage): ") / 100 / 12
    months = get_float_input("Enter the number of months you plan to repay the bond: ")

    repayment = house_value * (interest_rate * (1 + interest_rate) ** months) / ((1 + interest_rate) ** months - 1)
    print(f"The monthly bond repayment is: {repayment}")

# End of the program