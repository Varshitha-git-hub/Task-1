def calculate_power(voltage,current):
    power=voltage*current
    return power
voltage=float(input("enter voltage:"))
current=float(input("enter current:"))
result=calculate_power(voltage,current)
print("calculated power:",result)
