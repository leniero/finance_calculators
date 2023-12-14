Finance Calculators

Introduction

"Finance Calculators" is a Python application designed to help users make basic financial calculations. It includes options for calculating interest on investments and monthly repayments on home loans.

Features

- Investment Calculator: Calculate the amount of interest you'll earn on an investment. Supports both simple and compound interest calculations.
- Bond Calculator: Determine the monthly repayment amount on a home loan.

Technical Details

- Core Functionality:
  - `get_float_input`: A utility function to prompt for and validate float input from the user.
- User Inputs:
  - Choice between 'investment' or 'bond'.
  - For investments: deposit amount, interest rate, number of years, and interest type (simple/compound).
  - For bonds: present value of the house, interest rate, and number of months for repayment.
- Calculations:
  - Investment: 
    - Simple Interest: `total = deposit * (1 + interest_rate * years)`
    - Compound Interest: `total = deposit * ((1 + interest_rate) ** years)`
  - Bond: `repayment = house_value * (interest_rate * (1 + interest_rate) ** months) / ((1 + interest_rate) ** months - 1)`

How to Use

1. Run the `finance_calculators.py` script.
2. Choose either 'investment' or 'bond' when prompted.
3. Enter the required details based on your choice.
4. The script will display the calculated result.

Contact

For more information or inquiries, please visit [www.leandro-niero.com](http://www.leandro-niero.com).
