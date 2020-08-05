# this version, you run normally via the IDE
# needed this package to use the ceil function to round up
import math


print("What do you want to calculate?")
print("type 'n' - for count of months,")
print("type 'a' - for annuity monthly payment,")
print("type 'p' - for credit principal")
choice = input()

if choice == "p":
    print("Enter monthly payment:")
    monthly_payment = float(input())
    print("Enter count of periods:")
    periods = int(input())
    print("Enter credit interest:")
    credit_interest = float(input())
    nominal_interest_rate = credit_interest / 100 / 12
    credit_principal = math.floor(monthly_payment / ((nominal_interest_rate * (1 + nominal_interest_rate) ** periods) / ((1 + nominal_interest_rate) ** periods - 1)))
    print("Your credit principal = " + str(credit_principal) + "!")
elif choice == "n":
    print("Enter credit principal:")
    credit_principal = int(input())
    print("Enter monthly payment:")
    monthly_payment = float(input())
    print("Enter credit interest:")
    credit_interest = float(input())
    nominal_interest_rate = credit_interest / 100 / 12
    periods = math.ceil(math.log(monthly_payment / (monthly_payment - nominal_interest_rate * credit_principal), 1 + nominal_interest_rate))
    if periods == 1:
        print("You need " + str(periods) + " month to repay this credit!")
    elif periods < 12:
        print("You need " + str(periods) + " months to repay this credit!")
    elif periods == 12:
        print("You need 1 year to repay this credit!")
    elif periods % 12 == 0:
        num_of_years = int(periods / 12)
        print("You need " + str(num_of_years) + " years to repay this credit!")
    else:
        num_of_years = int(periods / 12)
        periods = periods % 12
        print("You need " + str(num_of_years) + " years and " + str(periods) + " months to repay this credit!")
elif choice == "a":
    print("Enter credit principal:")
    credit_principal = int(input())
    print("Enter count of periods:")
    periods = int(input())
    print("Enter credit interest:")
    credit_interest = float(input())
    nominal_interest_rate = credit_interest / 100 / 12
    annuity_payment = math.ceil(credit_principal * (nominal_interest_rate * (1 + nominal_interest_rate) ** periods) / ((1 + nominal_interest_rate) ** periods - 1))
    print("Your annuity payment = " + str(annuity_payment) + "!")
else:
    print("Your selection is incorrect")
