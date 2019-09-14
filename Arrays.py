from array import *

#Setting the array output
arr = array('i',[])
#Creating the string output 
n = int(input("Enter the length of the Array"))

#The  most times you can enter a value is the entered figure between the brackets below.
for i in range(4):

    x = int(input("Enter the next value"))
    arr.append(x)

print(arr) 


val = int(input("Enter the value for the search"))

k=0

for e in arr:
    if e==val:
        print(k)
        break
    k+=1