import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.c_int):
    pass

class Y(ctypes.c_int):
    pass

class Z(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

# verify that the _fields_ is read only
try:
    Z._fields_.append(('a', ctypes.c_int))
except AttributeError:
    pass
else:
    print('expected AttributeError')

# try to change the field type:
try:
    Z.x = X
except AttributeError:
    pass
else:
    print('expected AttributeError')

# try to add a new field:
try:
    Z.a = X
except AttributeError:
    pass
else:
    print('expected AttributeError')

# Now create an instance, and check that the fields are there
z = Z()
print(z.x, z.y, z.z)


