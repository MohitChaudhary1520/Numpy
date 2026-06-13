# BOOLEAN MASKING in which we fiter data on the basis of conditions..

import numpy as np

arr = np.array([10,27,30,43,51,61])
print(arr[arr>30])
print(arr[arr%2==0])