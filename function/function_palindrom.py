def int(n):
    rev = 0
    
    while(n>0):
        rev = (rev * 10) + n%10
        n = n // 10
    return rev

n= int(input("Please Enter any Num: "))



rev = (n)
# print("rev = %d" %rev)

if(n == rev):
    print("%d is a Palindrome" %n)
else:
    print("%d is not a palindrome number" %n)