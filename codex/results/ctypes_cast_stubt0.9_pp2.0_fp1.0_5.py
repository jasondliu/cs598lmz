import ctypes
ctypes.cast(X.ctypes.data,ctypes.POINTER(ctypes.c_int))

# ndarry.base tells you about it's actual buffer
X.base is X

# view shares the same data:
Y = X.view()
Y is X
Y.base is X
X[0] = 100
Y

# shallow copy also returns a view
Y = np.copy(X)
Y is X
Y.base is X
X[0] = 100
Y

# deep copy
Y = np.copy(X.flat)
Y is X
Y.base is X
X[0] = 100
Y

Y_flat = X.view() # returns a 1D view
Y_flat.base is X

Y_flat = X.flatten() # returns a copy
Y_flat.base is X


X.ravel() # also returns a view

# if matrix is not contiguous, it does a copy
Y = X.reshape((50,2))
Y.base is X


# Transposing is a view:
Y = X.T
Y.
