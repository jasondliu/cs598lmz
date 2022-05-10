import ctypes
ctypes.cast(a,ctypes.c_void_p).value

type(a)
len(a)
a.shape
a.size

np.arange(5)
np.arange(5,10)
np.arange(5,10,2)

np.linspace(0,100,11)

np.zeros(5) # 1-d array
np.zeros([5,5]) # 2-d array
np.zeros((5,5)) # 2-d array

np.ones(5) # 1-d array
np.ones([5,5]) # 2-d array
np.ones((5,5)) # 2-d array

np.random.randint(0,10,(5,5))
np.random.randint(0,10,size=(5,5))

np.random.randint(0,10,(3,3,3,3))
np.random.randint(0,10,size=(3,3,3,3))

np.random.random((5,5))
np.
