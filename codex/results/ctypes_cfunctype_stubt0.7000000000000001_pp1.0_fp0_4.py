import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return {}
</code>
The compilation of the file above yields a segfault:
<code>$ python test.py
Segmentation fault
</code>
My research on the internet did not lead me to an answer; some answers are available here (e.g., this one), but they are not helpful in my case.
I am using:

Python 3.6.5
GCC 7.3.0

What's wrong with the code above?

