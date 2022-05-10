import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

print fun()
</code>
But I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    print fun()
  File "test.py", line 4, in fun
    return "hello world"
TypeError: must be string without null bytes, not str
</code>
I have tried to use <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code> but it doesn't work either.
I am using Python 2.7.
Any ideas?


A:

I think you need to use <code>ctypes.c_char_p</code> as return type and <code>ctypes.create_string_buffer</code> to create the return string.
<code>import ctypes

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)

@FUNTYPE
def fun():
    return ctypes.create_string_buffer("hello world")
