def add(num1, num2):
    return num1 + num2
  
def subtract(num1, num2):
    return num1 - num2
  
def multiply(num1, num2):
    return num1 * num2
  
def divide(num1, num2):
    return num1 / num2


print("Please select operation -\n" ,"1. Add\n" ,"2. Subtract\n" ,"3. Multiply\n" ,"4. Divide\n")
  
selection = int(input("Select operations form 1, 2, 3, 4 :"))
  
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
  
if selection == 1:
    print(number1+number2)
  
elif selection == 2:
    print(number1-number2)
  
elif selection == 3:
    print(number1*number2)
  
elif selection == 4:
    print(number1/number2)
else:
    print("Invalid input")