# my_dictionary = {"name": "Kristina", "surname": "Beinoryte"}
# print(my_dictionary["name"])

# # my_dictionary["phone"] = 123456
# # print(my_dictionary["phone"])

# # my_dictionary["car"] = "Tesla"
# # print(f"my favourite car: {my_dictionary['car']}")

# my_dictionary["name"] = "Dom"
# print(my_dictionary)

# print(my_dictionary.keys())

# my_set = {1, 2, 3, 1, 1, 1}
# my_set.add(5)
# print(my_set)

# Write python program that asks user 
# to enter name, surname, age. 
# Put these values into a dictionary 
# and print dictionary
# Try creating structure like one here: l
# ink from an empty dictionary: my_dict = {}


# name = input("enter your name: ")
# surname = input("enter yor surname: ")
# age = int(input("enter your age: ")

# my_dictionary = {"name": name, "surname": surname, "age": age}
# print(my_dictionary)

# my_dictionary = {}
# my_dictionary["name"] = name
# my_dictionary["surname"] = surname
# my_dictionary["age"] = age
# print(my_dictionary)

# Str User name is "vardas", user surname is
#  "pavarde", users age is "amzius"

# print(f"User name is: {my_dictionary['name']}, User surname is: {my_dictionary['surname']}, Users age is: {my_dictionary['age']}")

# print(f"surname: {my_dictionary['surname']}")

# my_dictionary["number"]


user_info = {
	"name": "Albert",
	"surname": "Einstein",
	"occupation": {
		"role": "Professor",
		"workplace": "University of Berlin"
	},
        "languages": ["German", "Latin", "Italian", "English", "French"]
}

name = input("Enter name: ")
surname = input("Enter surname:")
my_dictionary = {"name": name, "surname": surname}
print(my_dictionary)

my_occupation = {"role": "Professor", "workplace": "University of Berlin"}
languages = ["German", "Latin", "Italian", "English", "French"]  
my_dictionary["occupation"] = my_occupation
my_dictionary["languages"]= languages
print(my_dictionary)