import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFuncPtr(ctypes.CFuncPtr):
    _flags_ = ctypes.ARG_COERCE

class _test(ctypes.Structure):
    _fields_ = [('func', CFuncPtr)]

def func(x, y):
    return x

ptr = _test()
ptr.func = func

val = ptr.func(1, 2)
print val
</code>
If you run this code with ctypes 1.0.2, it prints 3. This is because on char** args, ctypes tries to cast the Python object to a string, as in
<code>if ((PyObject_TypeCheck(src, &amp;PyString_Type) ||
     PyObject_TypeCheck(src, &amp;PyUnicode_Type)) &amp;&amp;
         (strlen(arg) &gt;= len) &amp;&amp; (arg[len] == '\0'))
</code>
This needs to be updated to respect the new <code>_flags_</code> field.

