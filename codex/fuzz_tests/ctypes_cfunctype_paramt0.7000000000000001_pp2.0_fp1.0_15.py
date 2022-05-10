import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)

def adder(a, b):
    return a + b

add_int = FUNTYPE(adder)
print add_int(1.0, 2.0)
</code>
I get the error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "c:\Python27\lib\ctypes\__init__.py", line 366, in __call__
    return self.call(*args)
ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: wrong type
</code>
Which indicates that the function that I passed in was not called, and only when <code>FUNTYPE</code> tried to call the Python function, it failed. 
What is the correct way to pass such a Python function to a C wrapper? 


A:

I'm not aware of any way to do this, but you could use the low level API to create a wrapper:

