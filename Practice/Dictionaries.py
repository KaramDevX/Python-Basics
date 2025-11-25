def easy_problem(string: str):
    words = string.split(" ")
    words_dict = {}
    for i in words:
        if i.lower() in words_dict:
            words_dict.update({i.lower():words_dict[i] + 1})
        else:
            words_dict.update({i.lower():1})
    print(words_dict)

# IMPROVED VERSION, direct assignment (.get() method) + better split
def easy_problem_s(string: str):
    words = string.split()
    words_dict = {}
    for i in words:
        words_dict[i.lower()] = words_dict.get(i.lower(), 0) + 1
    print(words_dict)   
#____________________________________________________________

def intermediate_problem(students: dict):
    passed = []
    for i in students:
        temp_list = []
        for j in students[i]:
            temp_list.append(j)
        if sum(temp_list)/len(temp_list) >= 75:
            passed.append(i)
    return passed

# IMPROVED VERSION, reduced redundancy (removing temp_list)
def intermediate_problem_s(students: dict):
    passed = []
    for i in students:
        if sum(students[i])/len(students) >= 75:
            passed.append(i)
    return passed
#____________________________________________________________


def hard_problem(inventory: dict):
    items_bought = {}
    print(f"Hello user, these are the current items available in store: \n{inventory}")
    while True:
        user_input = input("If you would like to buy an item, enter 'b'; If you want to leave at any point, enter 'e': ")

        if user_input == "e":
            break

        elif user_input == "b":
            while True:
                user_input = input("What would you like to buy: ")

                if user_input == "e":
                    break

                if user_input in inventory:

                    if inventory[user_input] > 0:
                        inventory[user_input] = inventory[user_input] - 1
                        print("Item Bought!")
                        print(f"Current inventory: {inventory}")

                        if user_input in items_bought:
                            items_bought.update({user_input: items_bought[user_input] + 1})

                        else:
                            items_bought.update({user_input: 1})

                    else:
                        print("That Item is out of stock")

                else:
                    print("Invalid Item")
    
        else:
            print("Invalid option")

        if user_input == "e":
            break

    return f"The items you bought are: {items_bought}"

# IMPROVED VERSION, removing nested while True loops, using direct assignment

def hard_problem_s(inventory: dict):
    items_bought = {}
    print(f"Hello user, these are the current items available in store: \n{inventory}")
    while True:
        user_input = input("If you would like to buy an item, enter 'b'; If you want to leave at any point, enter 'e': ")
        if user_input == "e":
            break
        elif user_input == "b":
            user_input = input("What would you like to buy: ")
            if user_input == "e":
                continue
            if user_input in inventory:
                if inventory[user_input] > 0:
                    inventory[user_input] = inventory[user_input] - 1
                    print("Item Bought!")
                    print(f"Current inventory: {inventory}")
                    items_bought[user_input] = items_bought.get(user_input, 0) + 1
                else:
                    print("That Item is out of stock")
            else:
                print("Invalid Item")
    
        else:
            print("Invalid option")

        if user_input == "e":
            break

    return f"The items you bought are: {items_bought}"
#___________________________________________________

inventory = {
    "flashlight": 3,
    "tent": 6,
    "bag": 1,
    "nuts": 2
}

# print(hard_problem(inventory))

# # students = {
#     "Ahmad": [65, 85, 93, 100, 35],
#     "Karam": [65, 100, 93, 22, 35],
#     "Hussein": [65, 10, 93, 22, 35]
# }

# print(intermediate_problem(students))

dict1 = {
    "brand": "Chanel",
    "Karam": "Hamad"
         }
print(dict1)
dict1.update({"brand": "Dior"})
print(dict1)
dict1.update({"Name": {"Karam": "Hamad"}})
print(dict1)
dict1["Name"].update({"Sanad": "Hamad"})
print(dict1)
print(dict1["Name"]["Karam"])

# for i in dict1:
#     print(f"{i}: {dict1[i]}")

