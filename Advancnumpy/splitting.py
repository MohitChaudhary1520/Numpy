'''
   dividing one array into multiple sub array
   1. np.split() #equally
   2. np.hsplit() #horizontally
   3. np.vsplit() #vertically
   
'''

import numpy as np

arr = np.array([10,20,30,40,50,60])

print(np.split(arr,3))
