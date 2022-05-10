import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print fun()
</code>
This works fine, but if I try to use a function that takes an argument, I get an error:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.c_int)
@FUNTYPE
def fun(a):
    return "hello"

print fun()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 5, in &lt;module&gt;
    print fun()
TypeError: this function takes exactly 1 argument (0 given)
</code>
I tried to use <code>ctypes.py_object(1)</code> as the argument, but I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 5, in &lt;module&gt;
    print fun(ctypes.py_object(1))
TypeError: an integer is required
</code>
What am I doing wrong?



