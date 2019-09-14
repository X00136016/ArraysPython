#Adding multiple dimensions to an array.
from numpy import *


arr = ones(5,int)

print('%.2f' %arr[0])


# array() linspace() logspace() arange() zeros() ones()
#Adding to arrays together
# min, max, sin, cos,log, sqrt concatenate

#defining the array list   
arr = array([1,2,3,4,5])


print(sqrt(arr))

#----------------------------------
arr = array([2,5,7,8,9])

arr1 = arr.copy()

arr[1]= 7


print(arr)
print(arr1)

print(id(arr))
print(id(arr1))