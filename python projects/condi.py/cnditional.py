#realtime example for conditional statements 
age=25
marks=75
x=10
y=20
if x>5:#if condition
    print("x is greater than 5")
if age>=18:
    print("you are eligible for vote!")
else:#else condition
    print("you are not eligible for vote!")
if marks>=90:
    print("grade:A")
elif marks>=75:#elif condition
    print("grade:B")
else:
    print("grade:C")
if x>5:
    if y>15:
        print("both conditions are true!")   
status="eligible" 
if age>=18:
    print("eligible")
else:
    print("Not Eligible")          

#Automatic coffee machine
coffee_type=input("what type of coffee do you want?(black coffee/coffee/cappuccino):")
sugar=input("do you want sugar?(yes/no):")
if coffee_type=="Black Coffee/black coffee":
    if sugar==yes:
        print("Here's your Black Coffee/black coffee with sugar!") 
    else:
        print("Here's your Black Coffee/black coffee without sugar!")   
elif coffee_type=="coffee/Coffee":
    if sugar==yes:
        print("Here's your coffee/Coffee with sugar!")
    else:
        print("Here's your coffee/Coffee without sugar!")
elif coffee_type=="cappuccino/Cappuccino":
    if sugar==yes:
        print("Here's your cappuccino with sugar!")
    else:
        print("Here's your cappuccino without sugar!")
else:
    print("sorry,we don't serve that type of coffee.")                     
    



