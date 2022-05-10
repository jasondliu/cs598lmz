import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

class C(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
        ('s', S * 10)
    ]

class D(ctypes.Structure):
    _fields_ = [
        ('c', C * 10)
    ]

d = D()

# Segmentation fault
d.c[9].s[9].x = 5
</code>
I am guessing the issue is the size of the C struct is too large? I am trying to simulate a 2D array.
Thanks
Update 1:
The following code works, but have to use a pointer, not sure if this is the best way of doing it:
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_int),
    ]

class C(ctypes.Structure):
    _fields_ = [
        ('s', S * 10)
    ]

class D(ctypes.Structure):
    _fields_ = [
