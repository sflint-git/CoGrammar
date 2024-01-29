# Create finance calculators for user
# Investment calculator should allow a user to calculate either simple or compound interest on their investment over a set period
# Bond calculator should calculate the amount the user will have to pay monthly on a bond over a set period of time

import math

# Explain calculators available and ask user to select one
explanation = '''There are two investment calculators available.
Investment - to calculate the amount of interest you'll earn on your investment.
Bond - to calculate the amount you'll have to pay on a home loan. '''

print(explanation)
print()
calculator_selected = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
calculator_selected_clean = calculator_selected.lower()

if (calculator_selected_clean != "investment") and (calculator_selected_clean != "bond"):
    new_calculator_selected = input("Your input is not valid. Please enter either 'investment' or 'bond': ")
    calculator_selected_clean = new_calculator_selected.lower()

# If investment calculator selected, allow user to calculate their investment with interest after the investment period
if calculator_selected_clean == "investment":
    deposit = float(input("Enter your deposit: £"))
    interest_pc = float(input("Enter the interest rate on your deposit: ")) / 100
    investment_period = float(input("Enter how long you plan to keep your deposit invested in years: "))
    interest = input("Is your interest rate 'simple' or 'compound': ").lower()
    
    if (interest != "simple") and (interest != "compound"):
        new_interest_selected = input("Your input is not valid. Please enter either simple or compound: ")
        interest = new_interest_selected.lower()

    if interest == "simple":
        total_investment = int(deposit * (1 + (interest_pc * investment_period)))
    elif interest == "compound":
        total_investment = int(deposit * math.pow((1+interest_pc), investment_period))
    print(f"Your total investment would be £{total_investment} after {int(investment_period)} years.")

# If bond calculator selected, calculate how much the user will need to repay each month
if calculator_selected_clean == "bond":
    bond_value = float(input("Enter the present value of your house: "))
    interest_rate = float(input("Enter the yearly rate of interest: ")) / 100 / 12
    months = float(input("Enter how many months you plan to repay the bond over: "))

    repayment = round((interest_rate * bond_value) / (1 - (1 + interest_rate) ** (-months)), 2)
    print(f"Your monthly repayments will be: £{repayment}.")