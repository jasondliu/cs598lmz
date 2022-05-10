import ctypes

class S(ctypes.Structure):
    x = ctypes.c_ubyte()
    y = ctypes.c_ubyte()
    z = ctypes.c_ubyte()

class U(ctypes.Union):
    _fields_ = [("a", ctypes.c_char * 1),
                ("b", S)]

print(S(), U().b, U().a)

#S(_0=0, _1=0, _2=0) S(_0=0, _1=0, _2=0) bytearray(b'\x00')
</code>
So the first print of S() isn't printing the value of the fields of S (x, y, z), but it is printing the values of the fields of S (a, b, c).
Can anyone tell me what is going on? 
Note: I'm using Python 3.7.1


A:

<code>ctypes</code>' <code>Structure</code> class's <code>__repr__</code> method calls <code>self._asdict()</code>, which in turn calls <code
