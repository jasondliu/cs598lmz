import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("bla")
    return 0
@FUNTYPE
def bla(*args):
    print(args)
    return args

bla(0, **dict(a=1, b=2))
</code>
I get an error:
<code>Traceback (most recent call last):
  File "D:\python_calll\tt.py", line 21, in &lt;module&gt;
    bla(0, **dict(a=1, b=2))
TypeError: bla() got an unexpected keyword argument 'a'
</code>
I guess it's because I return PyObject* and a keyword list is not a valid PyObject. How can I return a dictionary from a function which can handle arbitrary keyword arguments and still keep the function type FUNTYPE?


A:

So I think I got it. I had to call pyarg_parselist. This is the working version of the code:
<code>import ctypes
import ctypes.util

libpython_path = ctypes.util.find_library("python27")
if libpython_path is None:
