import numpy as np


a = np.array([1, 2, 3, 4, 5, 6])
print(a)

# create a simple array with numpy empty()
a = np.empty(9, dtype=object)
print(a)

# create multi-dim array by providing shape
matrix = np.empty(shape=(2, 5), dtype='object')
print(matrix)