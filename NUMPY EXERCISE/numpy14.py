# 13.counting of "P"
import numpy as np
a=np.array(['panther','python','apple','tiger','path'],dtype=str)
b=np.char.count(a,"p")
print(b)
lst=[]
lst.append(b)
d=np.sum(lst)

print("total no of p is ",d)

# 14.Write a Python program to find the maximum and 
# minimum value of a given flattened array.

a=np.arange(6).reshape(2,3)
print(a)
print(np.max(a))
print(np.min(a))

# 15. Write a NumPy program to get the minimum and maximum value of a given
#  array along the second axis.

x = np.arange(4).reshape((2, 2))
print("\nOriginal array:")
print(x)
print("\nMaximum value along the second axis:")
print(np.amax(x, 2))
print("Minimum value along the second axis:")
print(np.amin(x, 2))

# 16.Write a NumPy program to calculate the difference between 
# the maximum and the minimum values of a given array along the second axis.
import numpy as np
x = np.arange(12).reshape((2, 6))
print("\nOriginal array:")
print(x)
r1 = np.ptp(x, 1)
r2 = np.amax(x, 1) - np.amin(x, 1)
assert np.allclose(r1, r2)
print("\nDifference between the maximum and the minimum values of the said array:")
print(r1)

# 17.Write a Python NumPy program to compute the weighted 
# average along the specified axis of a given flattened array.
import numpy as np
a = np.arange(9).reshape((3,3))
print("Original flattened array:")
print(a)
print("Weighted average along the specified axis of the above flattened array:")
print(np.average(a, axis=1, weights=[1./4, 2./4, 2./4]))
