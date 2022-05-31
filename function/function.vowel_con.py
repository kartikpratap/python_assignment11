def value(val):
    vw=0
    cons=0
    for i in val:
        if i in ['a','e','i','o','u']:
            vw=vw+1
            print(i,"the vowel is \n")
        else:
            cons=cons+1
            print(i,"the consonet is")
    
    print("the vowels is given below\n",vw)

    print("the consonents are given below\n",cons)
val=input("enter the word for checking")
value(val)
