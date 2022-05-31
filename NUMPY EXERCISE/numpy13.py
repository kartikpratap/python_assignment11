# 8.Write a NumPy program to split the element of a given array with spaces.
import numpy as np
a=np.array(['taj','is','in','agra'], dtype=np.str)
b=np.char.split(a)
print(b)

# 9.Write a NumPy program to split the element of a given array to multiple lines.
c=np.array(['topics,on,numpy,are,given'])
d=np.char.splitlines(c)

print(d)

# 10.Write a NumPy program to make all the elements of a given string to a
#  numeric string of 5 digits with zeros on its left.
e=np.array([2,34,45,667,89,1],dtype=str)
f=np.char.zfill(e,5)
print(f)

# 11.. Write a NumPy program to replace PHP with Python 
# in the element of a given array

g=np.array(['PHP','PYTHON','PROGRAM','CODE'],dtype=str)
h=np.char.replace(g,"PHP","PYTHON")
print(h)

# 12.Write a NumPy program to test equal, not equal, greater equal, 
# greater and less test of all the elements of two given arrays.
x1 = np.array(['Hello', 'PHP', 'JS', 'examples', 'html'], dtype=np.str)
x2 = np.array(['Hello', 'php', 'Java', 'examples', 'html'], dtype=np.str)
print("\nArray1:")
print(x1)
print("Array2:")
print(x2)
print("\nEqual test:")
r = np.char.equal(x1, x2)
print(r)
print("\nNot equal test:")
r = np.char.not_equal(x1, x2)
print(r)
print("\nLess equal test:")
r = np.char.less_equal(x1, x2)
print(r)
print("\nGreater equal test:")
r = np.char.greater_equal(x1, x2)
print(r)
print("\nLess test:")
r = np.char.less(x1, x2)
print(r)