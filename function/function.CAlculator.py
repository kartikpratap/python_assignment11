print("SIMPLE CALCULATOR PROGRAM")
print("****************************************")
def addition(a,b):
    return a+b
def subtraction(a,b):


    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

print("selection of the operators\n","1\n","2\n","3\n","4\n")
selection=int(input("select the operator from 1,2,3,4\n"))
a=float(input("enter the first value\n"))
b=float(input("enter the second value\n"))

if selection==1:
    print(a+b)
elif selection==2:

    print(a-b)
elif selection==3:
    print(a*b)
elif selection==4:
    print(a/b)
else:
    print("invalid input\n")