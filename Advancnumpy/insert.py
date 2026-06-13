'''
np.insert(array,index,value,axis=0)
array - array name
index - index value
value - which value
axis -
axis=0 for row in 2d
axis=1 for column in 2d

'''
import numpy as np

arr = np.array([1,20,40,50,8])
print(arr)
arr2 = np.insert(arr,3,33)
print(arr2)