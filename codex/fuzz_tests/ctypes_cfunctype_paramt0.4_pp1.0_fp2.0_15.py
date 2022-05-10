import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

# set up a function pointer
func = FUNTYPE(None)

# set the function pointer to a function
func = FUNTYPE(lambda: None)

# set the function pointer to another function
func = FUNTYPE(lambda x: None)
</code>
The first two lines work fine, but the third line raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    func = FUNTYPE(lambda x: None)
ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type
</code>
Why is this?  The function pointer is set to a function that accepts one argument.  How can I fix this?


A:

You must specify the argument types for the function pointer.  The first function pointer is set to a function that accepts no arguments, so the argument types are <code>None</code>.  The second function pointer is set to a function that accepts no arguments, so the argument types are <code>None</code>.  The third function pointer is
