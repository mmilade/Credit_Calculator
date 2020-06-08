# needed this package to use the ceil function to round up
import math

print("Enter the credit principal:")
credit_principal = int(input())
print("What do you want to calculate?")
print("type 'm' - for count of months")
print("type 'p' - for monthly payment")
choice = input()

if choice == "p":
    print("Enter count of months:")
    num_of_months = int(input())
    if credit_principal % num_of_months == 0:  # check if number if month is a whole number
        monthly_payment = credit_principal/num_of_months
        print("Your monthly payment = " + str(monthly_payment))
    else:
        monthly_payment = math.ceil(credit_principal / num_of_months)  # ceil function rounds up
        last_payment = credit_principal - (num_of_months - 1) * monthly_payment  # formula
        print("Your monthly payment = " + str(monthly_payment) + " with last month payment = " + str(last_payment))
elif choice == "m":
    print("Enter monthly payment:")
    monthly_payment = int(input())
    num_of_months = round(credit_principal / monthly_payment)
    if num_of_months > 1:
        print("It takes " + str(num_of_months) + " months to repay the credit")
    else:
        print("It takes " + str(num_of_months) + " month to repay the credit")
else:
    print("Your selection is incorrect")




# I don't understand why this is not working

# def input_credit_principal():
#     print("Enter the credit principal:")
#     credit_principal = int(input())
#     return credit_principal
#
#
# def user_choice(credit_principal):
#     print("What do you want to calculate?")
#     print("type 'm' - for count of months")
#     print("type 'p' - for monthly payment")
#     choice = input()
#     if choice == "p":
#         show_payments(credit_principal)
#     elif choice == "m":
#         show_months(credit_principal)
#     else:
#         print("Your selection is incorrect")
#
#
# def show_payments():
#     print("Enter count of months:")
#     num_of_months = int(input())
#     if credit_principal % num_of_months == 0:
#         monthly_payment = credit_principal/num_of_months
#         print("Your monthly payment = " + str(monthly_payment))
#     else:
#         monthly_payment = round(credit_principal / num_of_months)
#         last_payment = credit_principal - (num_of_months - 1) * monthly_payment
#         print("Your monthly payment = " + str(monthly_payment) + " with last month payment = " + str(last_payment))
#
#
# def show_months():
#     print("Enter monthly payment:")
#     monthly_payment = int(input())
#     num_of_months = int(credit_principal / monthly_payment)
#     if num_of_months > 1:
#         print("It takes " + str(num_of_months) + " months to repay the credit")
#     else:
#         print("It takes " + str(num_of_months) + " month to repay the credit")
#
#
# input_credit_principal()
# user_choice()