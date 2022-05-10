import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
#define a callback function
def py_callback(arg):
    return arg

#convert function object to callback function object
fun = FUNTYPE(py_callback)

#get a lib object
lib = ctypes.cdll.LoadLibrary("./_add.so")
#set the callback function into lib object
lib.set_callback(fun)
#call the function in lib object
print lib.call_test(3)
#call the function in lib object again
print lib.call_test(4)
</code>
It works in python2 ,but not in python3.
I get the following error:
<code>Traceback (most recent call last):
File "py_callback.py", line 18, in &lt;module&gt;
print lib.call_test(3)
File "/usr/lib/python3.5/ctypes/__init__.py", line 377, in __getattr__
func = self.__getitem__(name)
File "/usr/lib/python3.5/ctypes
