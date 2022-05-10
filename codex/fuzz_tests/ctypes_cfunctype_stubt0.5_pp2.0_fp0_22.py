import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

print(fun())
</code>
This works as expected, and prints <code>Hello</code>.
However, if I use <code>ctypes.c_char_p</code> instead of <code>ctypes.py_object</code>, I get an error:
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_char_p)
&gt;&gt;&gt; @FUNTYPE
... def fun():
...     return "Hello"
...
&gt;&gt;&gt; print(fun())
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type
</code>
Why is this?


A:

You need to convert your return value to a <code>ctypes.c_char_p</code> object
