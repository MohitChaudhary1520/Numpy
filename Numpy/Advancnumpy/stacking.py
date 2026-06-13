'''
   combine multiple arrays...using two function..
   1. vstack -> rowwise.. #vertically
   2. hstack -> columnwise..  #horizontally
   
'''

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.array([7,8,9])

print(np.vstack((arr1,arr2,arr3)))
print(np.hstack((arr1,arr2,arr3)))

