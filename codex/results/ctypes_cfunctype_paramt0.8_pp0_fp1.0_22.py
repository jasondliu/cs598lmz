import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)
FUN_op_function = FUNTYPE(op_function)
</code>
Which gives me this error message:
<code>ctypes.ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: incompatible function   
arguments. Arguments should be of  ctypes.c_void_p type,
but are type 'LONG_PTR'
</code>
As suggested in this question I tried to change the type of op_function to LONG_PTR, which is done like this in python:
<code>def op_function(d_long):
    print "some code"

op_function.restype = ctypes.c_void_p # LONG_PTR
op_function.argtypes = [ctypes.c_void_p] #LONG_PTR
</code>
but now I get this error:
<code>Process finished with exit code -1073741819 (0xC0000005)
</code>
In the question I linked there is no suggestion of how to solve this problem. So my question
