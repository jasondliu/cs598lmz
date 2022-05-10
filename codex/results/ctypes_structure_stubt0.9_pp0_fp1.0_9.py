import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    x = ctypes.c_int
</code>
But I'm getting:
<code>    x = ctypes.c_int
NameError: name 'x' is not defined
</code>
Is this legal in python, or do I have to do it some other way?


A:

<code>ctypes</code> attributes must be defined right in the class definition. You cannot have locally scoped names there. That's just how <code>ctypes</code> is implemented.

