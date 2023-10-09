# weight_lower_limit: float = 75.5
# weight_higher_limit: float = 100.0

# weight_user = float(input("enter your weight: "))

# if weight_user < weight_lower_limit:
#     print("Mindaugas is new")
# elif weight_user > weight_higher_limit:
#     print("Mindaugas is young")
# else:
#     print("Mindaugas is cool")


# Task nr. 1
# Text
# Create a program, which takes 10 random numbers.
# The program should produce
# a list of non primary and tuple of primary numbers.
# After input is done, program should return the 
# the mathematical
# differnce between the highest and 
# lowest number from non primary numbers, 
# and sum of primary numbers from tuple.

# Task 
# rogram takes 3 random numbers as user input. 
# Update lsit and tuple data 
# structures with those values and print it.




# my_list = []
# number_one = input("Enter first number: ")
# number_two = input("Enter second number: ")
# number_three = input("Enter third number: ")
# my_list.append(number_one)
# my_list.append(number_two)
# my_list.append(number_three)

# my_tuple = (number_one, number_two, number_three)

# print(my_list)
# print(my_tuple)

number_1 = int(input("Enter 1 number: "))
number_2 = int(input("Enter 2 number: "))
number_3 = int(input("Enter 3 number: "))
number_4 = int(input("Enter 4 number: "))
number_5 = int(input("Enter 5 number: "))
number_6 = int(input("Enter 6 number: "))
number_7 = int(input("Enter 7 number: "))
number_8 = int(input("Enter 8 number: "))
number_9 = int(input("Enter 9 number: "))
number_10 = int(input("Enter 10 number: "))


my_list = []
my_tuple_list = []
if number_1 < 50:
    my_list.append(number_1)
else: 
    my_tuple_list.append(number_1)
if number_2 < 50:
    my_list.append(number_2)
else: 
    my_tuple_list.append(number_2)
if number_3 < 50:
    my_list.append(number_3)
else: 
    my_tuple_list.append(number_3)
if number_4 < 50:
    my_list.append(number_4)
else: 
    my_tuple_list.append(number_4)
if number_5 < 50:
    my_list.append(number_5)
else: 
    my_tuple_list.append(number_5)
if number_6 < 50:
    my_list.append(number_6)
else: 
    my_tuple_list.append(number_6)
if number_7 < 50:
    my_list.append(number_7)
else: 
    my_tuple_list.append(number_7)
if number_8 < 50:
    my_list.append(number_8)
else: 
    my_tuple_list.append(number_8)
if number_9 < 50:
    my_list.append(number_9)
else: 
    my_tuple_list.append(number_9)
if number_10 < 50:
    my_list.append(number_10)
else: 
    my_tuple_list.append(number_10)

print(my_list)
print(tuple(my_tuple_list))


print(max(my_list) - min(my_list))


