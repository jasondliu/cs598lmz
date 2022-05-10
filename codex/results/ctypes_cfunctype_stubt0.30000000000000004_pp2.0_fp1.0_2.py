import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "&lt;stdin&gt;", line 2, in fun
TypeError: 'str' does not have the buffer interface
</code>
I have tried to use the <code>ctypes.create_string_buffer</code> function, but it seems to be for C strings, not Python strings.
How can I return a Python string from a C function?


A:

You can't, because Python strings are not compatible with the C calling convention.
The C calling convention is a set of rules for passing parameters to and from functions, and returning values from functions.  The C calling convention is used by default in CPython, so it's what you're using when you call <code>ctypes.CFUNCTYPE</code>.
Python strings are not compatible with the C calling convention, because they are reference counted.  The C calling convention does not support reference counting.  The
