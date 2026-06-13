# SHAPE OF MATRIX >>> MEANS ROWS AND COLUMN.....

# import numpy as np
# arr_2d = np.array([[1,2,3],
#                    [4,5,6]])
# print(arr_2d.shape)

# SIZE OF ARRAY>>> mEANS TOTAL NUMBER OF ELEMENT IN AN ARRAY>>>

# import numpy as np
# arr_3d = np.array([[1,2,3],
#                    [4,5,6],
#                    [7,8,9]])
# print(arr_3d.size)

# NDIM OF ARRAY>>>>> MEANS NO OF DIMENSION IN AN ARRAY>>>>>

# import numpy as np
# arr1 = np.array([1,2,3])
# arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# arr3 = np.array([[[1,2],[3,4],[5,6],[7,8]]])

# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)

# DTYPE OF ARRAY>>>>> MEANS DATATYPE OF ELEMENTS IN AN ARRAY>>>>>>

# import numpy as np
# arr1 = np.array([1,2,3])
# arr2 = np.array([[1,2,3],[4,5.0,6],[7,8,9]])
# arr3 = np.array([[[1,2],[3,4],[5,6],[7,8]]])

# print(arr1.dtype)
# print(arr2.dtype)
# print(arr3.dtype)

# ASTYPE >>>> MEANS CHANGE DATATYPE OF ARRAY>>>>>>

import numpy as np

arr1 = np.array([1.0,2.4,3.5])
print(arr1.dtype)

int_arr = arr1.astype(int)
print(int_arr)
print(int_arr.dtype)