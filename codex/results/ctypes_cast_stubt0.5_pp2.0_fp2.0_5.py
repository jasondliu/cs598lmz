import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#Numpy
import numpy as np
x = np.random.randint(10, size=(3, 4, 5))
print(x)
print(x[0,0,0])

#Boolean Indexing
x = np.array([[1,2],[3,4],[5,6]])
print(x)
print(x[x>2])
print(x[x>2].shape)

#Axis
x = np.array([[1,2],[3,4]])
print(x.sum(axis=0))
print(x.sum(axis=1))

#Reshape
x = np.array([[1,2],[3,4]])
print(x.reshape(1,4))

#Concatenate
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
print(np.concatenate((x,y),axis=0))
print(np.
