import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint64()
    y = ctypes.c_uint64()

s = S()

# I'd like to do something like this:
# s.x &= 0xFFFFFFFF
# s.y &= 0xFFFFFFFF
# but I can't figure out how to do it.
</code>
Is there a way to do this in Python 2.7.3?


A:

You can't do this with a <code>ctypes.Structure</code> object.  You have to use the <code>_[type]_</code> attribute of the object to access the underlying C value, and then you can use the <code>from_address()</code> method of the <code>ctypes</code> module to access this value.
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_uint64),
                ('y', ctypes.c_uint64)]

s = S()

print(s.x)         # Prints 0
s.x = ctypes
