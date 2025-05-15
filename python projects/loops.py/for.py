# Project Overview:
#     This project is a simple shopping list program that allows users to add items to their shopping list and then displays the list.

# code:
num_items = int(input("How many items do you want to add to your shopping list? "))

shopping_list = []

for i in range(num_items):
    item = input(f"Enter item {i+1}: ")
    shopping_list.append(item)

print("\nYour Shopping List:")
for i, item in enumerate(shopping_list):
    print(f"{i+1}. {item}")
 
#  How it works:
#  1.The program first asks the user how many items they want to add their shopping list.
#  2.The user is then prompted to enter each item,one by one.
#  3.The program stores each item in a list caled shopping list.
#  4.Once all items have been entered, the program displays the complete shopping list.
 
# Key Features:
#  1.User input for number of items and item names.
#  2.Storage of items in a list.
#  3.Display of complete shopping list.

# Example Usage:
#  1.User runs the program and is asked how many items they want to add.
#  2.User enter3 and is then prompted to enter each item(eg:"milk","bread","eggs").
#  3.Program displays the complete shopping list:
# Your shopping list:
#  1.Milk
# 2.Bread
# 3.Eggs
