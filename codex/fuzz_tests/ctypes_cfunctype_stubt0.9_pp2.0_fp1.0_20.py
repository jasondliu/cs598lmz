import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 12345

print('fun() =',fun())
</code>
In this case, you'll see <code>fun() = &lt;__main__.NON_PYTHON_FUNCTYPE object at 0x00000000020BDE48&gt;</code> as the output. This is because we created the function on the fly and the function is obviously not the same as the functions generated by <code>py_object</code>.
<code>NON_PYTHON_FUNCTYPE</code> is just for signing to keep them separate.
This means that you can create functions that don't go through the <code>PyObject*</code> path and instead use the <code>@NON_PYTHON_FUNTYPE</code> decorator.
Please note
The <code>NON_PYTHON_FUNTYPE</code> decorator is just a quick hack to make it work.
Ultimately, I want to add <code>@ctypes.IN</code> and <code>@ctypes.OUT</code> and <code>@ctypes.FUNCTION_C
