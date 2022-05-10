import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

def function(x):
    return x**2

f = FUNTYPE(function)
print(f(2))
</code>
I am getting the following error:
<code>Traceback (most recent call last):
  File "C:/Users/saurabh/Desktop/Python_Projects/Pygame/FFI.py", line 10, in &lt;module&gt;
    f = FUNTYPE(function)
  File "C:\Users\saurabh\AppData\Local\Programs\Python\Python36-32\lib\ctypes\__init__.py", line 364, in __call__
    self._errcheck(*args)
  File "C:\Users\saurabh\AppData\Local\Programs\Python\Python36-32\lib\ctypes\__init__.py", line 371, in _errcheck
    raise TypeError(msg)
TypeError: Incorrect argument type (expected c_double, got float)
</code>
What I want to know is that why is the
