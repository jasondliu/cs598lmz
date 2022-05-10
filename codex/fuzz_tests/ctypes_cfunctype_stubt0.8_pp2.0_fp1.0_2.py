import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

fun()
</code>
The only thing I can find is this SO post that recommends <code>visibility='protected'</code>.  However, doing that gives me the same error.


A:

By default, a Python function cannot be called directly by C++:
<blockquote>
<p>When the module is loaded by Python, a wrapper object is created which
  acts like a Python object, but calls C functions (and thus the user’s
  code) when accessed.</p>
</blockquote>
To enable this, call <code>enable_function</code> on the function:
<code>...
fun = mod.get_function("fun")
fun.enable_function()
</code>

