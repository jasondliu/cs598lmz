import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
@FUNTYPE
def fun1():
    return "abc"
s = fun()
print s
s = fun1()
print s
</code>
On Python 2.6, it prints
<code>None
abc
</code>
but on 2.7, it gives
<code>AttributeError: 'str' object has no attribute '__reduce__'
</code>
I read the documentation and it says that the callable object should return None, True, False, or a numeric value. So why do I get the AttributeError?
Note: I have installed ctypes on Python 2.6 and 2.7 in the virtualenv (as a workaround to this) and using Linux.
Update: I checked ctypes on 32 bit Python 2.6 and 32 bit Python 2.7 and both seem to be working fine. I am now more sure of this being a bug. So please anyone direct me to the Python bug tracker and possibly assign me the necessary rights!


A:

For 2.6 the docs says about create_string_buffer:
<blockquote>
<p>Return type: ctypes.py_
