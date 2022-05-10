import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
def c_test(test_func):
    test_func = FUNTYPE(test_func)
    ctypes.pythonapi.Py_InitModule4(
        "c_test",
        ctypes.py_object(ctypes.pythonapi),
        ctypes.py_object(0),
        ctypes.py_object(0),
        ctypes.py_object(0)
    )
    ctypes.pythonapi.PyObject_SetAttrString(
        ctypes.py_object(ctypes.pythonapi),
        "c_test",
        ctypes.py_object(test_func)
    )
    del test_func

def run_c_test(num):
    print(num)

c_test(run_c_test)
</code>
It works perfectly and as expected, as long as I don't call the <code>c_test</code> function more than once.
I'm not sure if this is a limitation of <code>ctypes</code> or <code>PyObject_SetAtt
