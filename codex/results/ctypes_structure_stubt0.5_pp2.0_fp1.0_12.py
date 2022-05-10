import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    def __init__(self):
        self.x = 5

s = S()
print s.x

s.x = 6
print s.x

# ctypes.c_int() is a factory function, which returns a new c_int object.
# for example,
print ctypes.c_int(5)

# ctypes.c_int() is not a constructor, it does not set the value of an existing object.
# for example,
print ctypes.c_int()

# ctypes.c_int() is not a member function, it does not set the value of an existing object.
# for example,
s.x = ctypes.c_int(5)
print s.x
</code>
The output is
<code>5
6
c_int(5)
c_int(0)
c_int(5)
</code>
I think the reason is that ctypes.c_int() is a factory function, it returns a new c_int object.
So, I think the following code is correct
