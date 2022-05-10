import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

c = C()
c.x = 42

# The following is not supported by ctypes, but we need it for
# testing.
c.__dict__['x'] = 43

print(c.x)
print(c.__dict__['x'])

# This is not supported by ctypes, but we need it for testing.
c.__dict__['x'] = 44

print(c.x)
print(c.__dict__['x'])

# This is not supported by ctypes, but we need it for testing.
c.__dict__['x'] = ctypes.c_int(45)

print(c.x)
print(c.__dict__['x'])

# This is not supported by ctypes, but we need it for testing.
c.__dict__['x'] = ctypes.c_int(46)

print(c.x)
print(c.__dict__['x'])
