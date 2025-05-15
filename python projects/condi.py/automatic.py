#project title:Automatic Coffee Machine
#Description:
#    This project simulates an automatic coffee machine that takes user input for the type of coffee and whether they want sugar or not. Based on the user's selection, the machine outputs the type of coffee and whether it's with or without sugar.
#Code:
coffee_type=input("what type of coffee do you want?(black coffee/coffee/cappuccino):")
sugar=input("do you want sugar?(yes/no):")
if coffee_type=="black coffee":
    if sugar=="yes":
        print("Here's your black coffee with sugar!")
    else:
        print("Here's your black coffee without sugar!")
elif coffee_type=="coffee":
    if sugar=="yes":
        print("Here's your coffee with sugar!")
    else:
        print("Here's your coffee without sugar!")
elif coffee_type=="cappuccino":
    if sugar=="yes":
        print("Here's your cappuccino with sugar!")
    else:
        print("Here's your cappuccino without sugar!")
else:
    print("sorry,we don't serve that type of coffee.")                                   
#key features:
# 1.user input for coffee type and sugar selection.
# 2.Conditional statements to check user input and provide output.
# 3.case-insensitive comparision for coffee type and sugar selection.
# 4.clear and conise output messages.        
#Technologies Used:
# 1.python programming language
# 2.conditional statements
# 3.input/output operations
#Benefits:
# 1.demonstrates the use of conditional statements in Python
# 2.provides a simpke and interactive way to simulates an automatic coffee machine
# 3.can be extended to include more features and functionality
#takeaway:
# 1.understand how to use conditional statements in python.
# 2.learn how to take user input and provide output based on that input
