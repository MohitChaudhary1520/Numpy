# np.isnan(array)
import numpy as np

arr = np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))

# we ccan not compare directly....
print(np.isnan == np.isnan)