import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 5
s.y = 4

s_p = ctypes.pointer(s)
s_p.contents.x = 10
</code>
The result is, that s.x = 10, but s.y = 4.
The reason is, that when you access s_p.contents, you are actually creating a new S object, thus losing all the data that s holds.
You could use the following hack to get what you want:
<code>import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
s.x = 5
s.y = 4

s_p = ctypes.pointer(s)

s_p.contents.contents = s
s_p.contents.contents.x = 10
</code>
This way, you assign s to s_p.contents.contents, and then alter s.x

