import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

fun()
</code>
The error message is:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;string&gt;", line 2, in fun
TypeError: invalid result type
</code>
I have tried to return a string, a list and a tuple. All of them give me a similar error message.
I have read the documentation of <code>ctypes</code> but it does not seem to have any information about this.
I am using Python 2.7.12.
How should I fix this problem?


A:

You have to use <code>ctypes.c_char_p</code> as the return type, not <code>ctypes.py_object</code>.
<code>&gt;&gt;&gt; ctypes.c_char_p
&lt;class 'ctypes.c_char_p'&gt;
&gt;&gt;&gt; ctypes.py_object
&lt
