number = int(input("input number = "))

part_one = number // 10000
print(part_one)

part_two = number % 10000 // 1000 
print(part_two)

part_three = number % 1000 // 100
print(part_three)

part_four = number % 100 // 10
print(part_four)

part_five = number % 10 // 1 
print(part_five)