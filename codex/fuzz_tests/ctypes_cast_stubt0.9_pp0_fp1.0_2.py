import ctypes
ctypes.cast(obj, ctypes.py_object).value

# set/get flag to request subtree in print tree
set_printoptions(threshold=obj.size*obj.itemsize)
# get the size of the datastructure in memory
obj.nbytes

# force numpy to have high precision
set_printoptions(precision=64)
np.set_printoptions(precision=64)

# addressing elements in 3D array
np.random.randint(9, size=(3,3,3))
np.random.randint(9, size=(3,3,3))[1,:,:]

# print integer numbers with leading zeros
# this will print 100 as 00100
print(str(100).zfill(5))

# another way of doing the above
print('%05d' % (100))

# print a string with a certain number of leading zero
print(format(100, "05"))

# print the class of a certain object
print(type(obj_name))

# to make class structure visible in vscode - View > Command Palette

