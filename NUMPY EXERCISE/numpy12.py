#1.Write a NumPy program to concatenate element-wise two arrays of string.
import numpy as np
a=np.array(['python','mohd'],dtype=np.str)
b=np.array(['program','ahsan'],dtype=np.str)
c=np.char.add(a,b)
print(c)

#2. Write a NumPy program to repeat all the elements three times of a given array of string.

d=np.array(['program','of','python','programming'],dtype=np.str)
e=np.char.multiply(d,3)
print("after multiply")

print(e)

#3.Write a NumPy program to capitalize the first letter, lowercase, 
#uppercase, swapcase, title-case of all the elements of a given array.

f=np.array(['whEre','Are','you','comIng','from'])
print("before performing the oprations")
print(f)
print("after performing the operations")
print(np.char.upper(f))
print(np.char.lower(f))
print(np.char.swapcase(f))
print(np.char.title(f))

#4.Write a NumPy program to make the length of each element 15 of a given array and 
 the string centered  left-justified right-justified with paddings of .

import numpy as np
x = np.array(['python exercises', 'PHP', 'java', 'C++'], dtype=np.str)
c= np.char.center(x, 15, fillchar='_')
l = np.char.ljust(x, 15, fillchar='_')
r = np.char.rjust(x, 15, fillchar='_')
print(c)
print( l)
print(r)

#5.Write a NumPy program to encode all the elements 
# of a given array in cp500 and decode it again.

y=np.array(['we','are','here','for','learning'],dtype=np.str)
en=np.char.encode(y,'cp500')
de=np.char.decode(en,'cp500')
print("after encoding the array\n")
print(en)
print("after decoding the encoded array")
print(de)

#6.. Write a NumPy program to remove the leading and trailing 
# whitespaces of all the elements of a given array.
j=np.array(['techonology','is','increasing','daybyday','in','india'])
g=np.char.lstrip(j)
print(g)

#7.Write a NumPy program to remove the 
# trailing whitespaces of all the elements of a given array
j=np.array(['techonology','is','increasing','daybyday','in','india'])
g=np.char.rstrip(j)
print(g)