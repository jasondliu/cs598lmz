import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

fun()
</code>
But when I run this code, I get the following error:
<blockquote>
<p>Traceback (most recent call last):   File "C:\Users\me\Desktop\test.py",
  line 8, in 
      fun()   File "C:\Users\me\Desktop\Python\Python37-32\lib\ctypes__init__.py", line 383, in <strong>call</strong>
      return self._function(*args) TypeError: argument 1 must be a string, not bytes</p>
</blockquote>
How can I return a string from the callback?


A:

I am running Python 3.7.0 on Windows 10.
This code works for me:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

print(fun())
</code>
I get the result <code>hello world</code>.

