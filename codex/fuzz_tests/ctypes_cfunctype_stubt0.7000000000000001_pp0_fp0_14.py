import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

"This is the test"
fun()
</code>
This will fail with a <code>ValueError</code> similar to:
<code>ValueError: native function 'fun' returned non-native type 'int'
</code>
You can find more information in the docs for <code>Py_SetProgramName</code>, which also mentions <code>Py_SetPythonHome</code>.

