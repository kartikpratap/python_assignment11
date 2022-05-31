def fun(S):
    # print("entered string is",S)
    n1=0
    n2=0
    for i in S:
        if i.islower():
            n1=n1+1
        elif i.isupper():
            n2=n2+1
    print("the uppercase is",n2)
    print("the loweracse is",n1)

S=str(input("enter the string\n"))
fun(S)