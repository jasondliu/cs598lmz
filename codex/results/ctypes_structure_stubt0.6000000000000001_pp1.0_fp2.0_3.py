import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(0)
    _fields_ = [("y", ctypes.c_int)]

S.x += 1
S.y += 1

print S.x, S.y
</code>
The output is:
<code>1 1
</code>
If you want to make the fields read-only, you can do it like this:
<code>import ctypes

class S(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

def set_x(self, value):
    self.__x = value

def set_y(self, value):
    self.__y = value

S.__x = S.x
S.x = property(lambda self: self.__x, set_x)
S.__y = S.y
S.y = property(lambda self: self.__y, set_y)

s = S()
print s.x, s.y
s.x = 2
s.y = 3

