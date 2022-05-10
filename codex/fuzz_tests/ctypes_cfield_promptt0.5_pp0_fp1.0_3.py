import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("f", ctypes.CField)]

x = X()
y = Y()

# Test that we can access the field
print x.a

# Test that we can assign to the field
x.a = 1
print x.a

# Test that we can assign to the field via the CField
y.f = x.a
print y.f

# Test that we can assign to the field via the CField
y.f = 2
print y.f

# Test that we can assign to the field via the CField
y.f = y.f + 1
print y.f

# Test that we can assign to the field via the CField
y.f += 1
print y.f

# Test that we can assign to the field via the CField
y.f -= 1
print y.f

# Test that we can assign to the field via the CField
y
