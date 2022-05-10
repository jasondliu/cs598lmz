import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32()
    y = ctypes.c_int32()

s = S()
s.x = 1
s.y = 2
print s.x
print s.y
</code>
This prints <code>1</code> and <code>2</code> as expected. But if I try to use <code>__slots__</code> to prevent the creation of <code>__dict__</code> for <code>S</code>, I get a <code>TypeError</code>:
<code>import ctypes

class S(ctypes.Structure):
    __slots__ = ['x', 'y']
    x = ctypes.c_int32()
    y = ctypes.c_int32()

s = S()
s.x = 1
s.y = 2
print s.x
print s.y
</code>
This prints <code>TypeError: object.__new__(S) is not safe, use ctypes.Structure.__new__()</code>.
I know I can use <code>__new
