# note that without key=int parameter, max will take the lexicographically-largest item
# i.e. 8 is greater than 11 as the first digit 8 is greater than the first digit 1

cafe_details = {}

while True:
    cafe_name = input()
    if cafe_name == 'MEOW':
        max_value = max(cafe_details.values(), key=int)
        for name, number in cafe_details.items():
            if number == max_value:
                print(name)
        break
    else:
        cafe_name_split = cafe_name.split()
        cafe_details[cafe_name_split[0]] = cafe_name_split[1]


# another solution
# cafes, cats = [], []
# while True:
#     cafe = input().split()
#     if cafe[0] == "MEOW":
#         break
#     cafes.append(cafe[0])
#     cats.append(int(cafe[1]))
# print(cafes[cats.index(max(cats))])