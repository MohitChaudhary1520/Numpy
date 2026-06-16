# np.nan_to_num(array, nan=value) default value = 0

import numpy as np

arr = np.array([1,2,np.nan,4,np.nan,6])

cleaned_arr = np.nan_to_num(arr, nan=7)
print(cleaned_arr)