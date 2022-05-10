import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
   return 42

fun()
#42
</code>
The same problem is happening with Kivy.
I'm not sure if I have to write a custom build of Python, or what.
Thanks.


A:

It's not clear what you mean by 'embedding the Kivy interpreter', but it sounds like you might be trying to use Python 3. The short answer is that at present, due to its use of PyPy, Kivy only works with Python 2.7.

