import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = [('x', ctypes.c_int)]

class C(ctypes.Structure):
    S_inst = S()
    _fields_ = [('S_inst', S)]

c = C()
c.S_inst.x = 1
print c.S_inst.x

c.S_inst = S()
c.S_inst.x = 2
print c.S_inst.x
</code>
Update:  I have reported this as a bug on the Python bug tracker.

