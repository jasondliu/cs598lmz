import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

def pyfunc(a):
   print(a[0])
   return 0

cfunc = FUNTYPE(pyfunc)

array_type = ctypes.c_int * 1
params = array_type(1)

ret = cfunc(params)
</code>
I am expecting the output <code>1</code>, however I am getting the following error:
<code>Traceback (most recent call last):
  File "so.py", line 14, in &lt;module&gt;
    ret = cfunc(params)
TypeError: argument 1: &lt;class 'TypeError'&gt;: wrong type
</code>
What is wrong with the code?


A:

You need to pass a pointer to the first element of the array.
<code>cfunc(params[0])
</code>

