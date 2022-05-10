import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"
print(fun())
</code>
The error I get is:
<code>python3.3/ctypes/_endian.py", line 103, in _other_endian
if _sys.byteorder == "little":
AttributeError: 'module' object has no attribute 'byteorder'
</code>
This error is on line 103 of the file <code>_endian.py</code> in the ctypes module:
<code>if _sys.byteorder == "little":
</code>
I am using Python 3.3 on Windows. I tried to find a solution for this, but I couldn't find it anywhere. I tried updating many things like my C compiler and some deals with Python, but I still can't get it to run correctly.
What should I do to get it to run correctly?


A:

Update on this issue:
I updated everything on my machine and now it runs correctly.
My compiler was updated to allow me to compile my C code into a DLL, and the issue is resolved.

