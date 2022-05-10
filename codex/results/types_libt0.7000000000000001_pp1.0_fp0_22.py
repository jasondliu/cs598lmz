import types
types.TupleType

# size and shape
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
a.size
a.shape

a = np.array([[1,2,3],[4,5,6]],dtype=np.float)
a.dtype

# reshape
a = np.array([[1,2,3],[4,5,6]])
a.shape
a.reshape(3,2)

# resize
a = np.array([[1,2,3],[4,5,6]])
a.shape
np.resize(a,(2,3))

# append
a = np.array([[1,2,3],[4,5,6]])
b = np.append(a,[[7,8,9]],axis=0)

# delete
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
np.delete(a,1,0) # 删除
