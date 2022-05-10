import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [("x", ctypes.c_int)]

S()
</code>
The code runs without error.

I'm using Python 3.2 on Linux.

EDIT:
I've just tried the same code in Python 2.7 and 3.2 on Windows.  The error is still there.

EDIT 2:
I've just tried on Python 2.7 on Linux, and I get the same error.  It's not an error in Python 3.2.

EDIT 3:
I've just tried on Python 3.1 on Linux, and I get the same error.  It's not an error in Python 3.2.

EDIT 4:
I've just tried on Python 2.6 on Linux, and I get the same error.  It's not an error in Python 3.2.

EDIT 5:
I've just tried on Python 2.7 on Windows, and I get the same error.  It's not an error in Python 3.2.


A:

This is a bug in Python 2.6 and 2.7, and it's fixed in
