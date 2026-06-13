'''
   array[start:stop:step]
   array[start:stop] start to stop-1
   array[::-1] give reverse array
   
   '''

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,0])

print(arr[:4]) # give 1 to 4 values
print(arr[-4:]) #give start to end-1 value
print(arr[::2]) # give start to end value
print(arr[::-1]) # give reverse array
print(arr[2:8])
print(arr[2:8:2]) # give every second element from start to end

