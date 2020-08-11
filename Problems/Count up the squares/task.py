# print("Enter a number: ")
number = int(input())
total = number
number_squared = number ** 2
total_of_number_squared = number_squared

while total != 0:
    # print("Enter a number: ")
    number = int(input())
    number_squared = number ** 2
    total += number
    total_of_number_squared += number_squared
    # print(total)
    # print(total_of_number_squared)


# print("out of loop")
# print(total)
# print("The sum of their squares is: ", total_of_number_squared)
print(total_of_number_squared)


# Another solution:
# sum = 0
# sum_squared = 0
# while True:
#     prompt = int(input())
#     sum += prompt
#     sum_squared += prompt ** 2
#     if sum == 0:
#         print(sum_squared)
#         break