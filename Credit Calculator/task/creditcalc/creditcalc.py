# this is a command line only program, i.e. you must run a command like the following to get it to work
# see end of code for examples on how to run it and what to expect

import math
import sys
import argparse

supplied_args = sys.argv

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("--type", help="indicates the type of payments: 'annuity' or 'diff' (differentiated).", type=str)
parser.add_argument("--payment", help="monthly payment", type=float)
parser.add_argument("--principal", help="used for calculations of both types of payment. You can get its value knowing the interest, annuity payment and periods.", type=float)
parser.add_argument("--periods", help="parameter denotes the number of months and/or years needed to repay the credit. It's calculated based on the interest, annuity payment and principal.", type=int)
parser.add_argument("--interest", help="is specified without a percent sign.", type=float)


args = parser.parse_args()
payment_type = args.type
credit_interest = args.interest
monthly_payment = args.payment
principal = args.principal
periods = args.periods


if monthly_payment is not None and monthly_payment < 0:
    print("Incorrect parameters - Negative values are not allowed - monthly payment")
    exit()
if principal is not None and principal < 0:
    print("Incorrect parameters - Negative values are not allowed - principal")
    exit()
if periods is not None and periods < 0:
    print("Incorrect parameters - Negative values are not allowed - periods")
    exit()
if credit_interest is None or credit_interest < 0:
    print("Incorrect parameters - Negative values are not allowed - credit_interest")
    exit()


if payment_type == "diff":
    if monthly_payment is not None:
        print("Incorrect parameters - payment shouldn't be specified")
    elif len(supplied_args) < 5:
        print("Incorrect parameters - Wrong number of parameters supplied")
elif payment_type == "annuity":
    if len(supplied_args) < 5:
        print("Incorrect parameters - Wrong number of parameters supplied")
else:
    print("Incorrect parameter - bad payment type")

# this is for testing purposes
# print("Payment Type is: ", payment_type)
# print("Credit Interest is: ", credit_interest)
# print("Monthly Payment is: ", monthly_payment)
# print("Credit Principal is: ", principal)
# print("Credit Periods is: ", periods)
# print("You've supplied", len(supplied_args), "arguments")


if monthly_payment is None:
    if payment_type == "diff":
        month_number = 1
        total_paid = 0
        nominal_interest_rate = credit_interest / 100 / 12

        while month_number <= periods:
            differentiated_payment = math.ceil((principal / periods) + nominal_interest_rate * (principal - (principal * (month_number - 1)) / periods))
            print(month_number, " : paid out ", differentiated_payment)
            month_number += 1
            total_paid = total_paid + differentiated_payment

        overpayment = int(total_paid - principal)
        print("Overpayment = ", overpayment)

    elif payment_type == "annuity":
        nominal_interest_rate = credit_interest / 100 / 12
        annuity_payment = math.ceil(principal * (nominal_interest_rate * (1 + nominal_interest_rate) ** periods) / ((1 + nominal_interest_rate) ** periods - 1))
        print("Your annuity payment = " + str(annuity_payment) + "!")
        overpayment = int((annuity_payment * periods) - principal)
        print("Overpayment = ", overpayment)
    else:
        print("wrong payment type")


if principal is None:
    nominal_interest_rate = credit_interest / 100 / 12
    principal = math.floor(monthly_payment / ((nominal_interest_rate * (1 + nominal_interest_rate) ** periods) / ((1 + nominal_interest_rate) ** periods - 1)))
    print("Your credit principal = " + str(principal) + "!")
    overpayment = int((monthly_payment * periods) - principal)
    print("Overpayment = ", overpayment)


if periods is None:
    nominal_interest_rate = credit_interest / 100 / 12
    periods = math.ceil(math.log(monthly_payment / (monthly_payment - nominal_interest_rate * principal), 1 + nominal_interest_rate))
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

    overpayment = int((monthly_payment * periods) - principal)
    print("Overpayment = ", overpayment)

# examples of how to run this program
# this is a command line only program, i.e. you must run a command like the following to get it to work
# > python credit_calc.py --type=diff --principal=1000000 --periods=10 --interest=10
# Month 1: paid out 108334
# Month 2: paid out 107500
# Month 3: paid out 106667
# Month 4: paid out 105834
# Month 5: paid out 105000
# Month 6: paid out 104167
# Month 7: paid out 103334
# Month 8: paid out 102500
# Month 9: paid out 101667
# Month 10: paid out 100834
#
# Overpayment = 45837
#
#
# > python credit_calc.py --type=annuity --principal=1000000 --periods=60 --interest=10
# Your annuity payment = 21248!
# Overpayment = 274880
#
# > python credit_calc.py --type=diff --principal=1000000 --payment=104000
# Incorrect parameters.
#
# > python credit_calc.py --type=diff --principal=500000 --periods=8 --interest=7.8
# Month 1: paid out 65750
# Month 2: paid out 65344
# Month 3: paid out 64938
# Month 4: paid out 64532
# Month 5: paid out 64125
# Month 6: paid out 63719
# Month 7: paid out 63313
# Month 8: paid out 62907
#
# Overpayment = 14628
#
# > python credit_calc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
# Your credit principal = 800018!
# Overpayment = 246622
#
# > python credit_calc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
# You need 2 years to repay this credit!
# Overpayment = 52000