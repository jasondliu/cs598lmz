import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16() # also fails if set to c_int
class N(ctypes.Structure):
    _fields_ = [('nested', S)]

x = N()
print x.nested.x.value == 0 # works
x.nested.x.value = 5
print x.nested.x.value == 5 # fails
</code>
In other words, x.nested.x.value is an int, but I cannot assign a value to it. Changing type from int16 to int does not help.
Any pointers? Thanks!


A:

I was able to find a solution, so here it is, in case anybody needs it.
What I was missing is that numpty.ctypes creates a totally new Python class when you call N.from_new(). My workaround is to copy the __dict__ properties from the new class over to the old class. Here is the working code:
import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int16() # must use ctypes.c_int16, ctypes.c_int fails
