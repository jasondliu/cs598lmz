import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

print(fun())
</code>
I get
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    print(fun())
TypeError: 'str' object is not callable
</code>
But if I do
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
@FUNTYPE
def fun():
    return "hello world"

print(fun())
</code>
I get
<code>hello world
</code>
What is happening here?


A:

<code>ctypes.py_object</code> is a pointer to a Python object, not a Python object itself.  You need to dereference it before passing it to <code>print</code>:
<code>print(fun()[0])
</code>

