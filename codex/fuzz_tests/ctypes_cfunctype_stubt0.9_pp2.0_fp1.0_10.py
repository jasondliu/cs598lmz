import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
  return 1

fun() # Returns 1
</code>
(The above is a Python 2 example.  In Python 3 you would return an <code>int</code> and change <code>c_types.py_object</code> to <code>c_types.py_object</code>.)
To get the address of the function, you can use <code>ctypes.addressof</code>:
<code>&gt;&gt;&gt; ctypes.addressof(fun)
&lt;built-in function fun&gt;
&gt;&gt;&gt; hex(ctypes.addressof(fun))
'0x1034b6c10'
</code>

