fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# The following should not crash
import ctypes
ctypes.pythonapi.PyThreadState_SetAsyncExc.argtypes = [ctypes.c_long, ctypes.py_object]
ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(0), ctypes.py_object(0))

# The following should not crash
import ctypes
ctypes.pythonapi.PyThreadState_SetAsyncExc.argtypes = [ctypes.c_long, ctypes.py_object]
ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(0), ctypes.py_object(0))

# The following should not crash
import ctypes
ctypes.pythonapi.PyThreadState_SetAsyncExc.argtypes = [ctypes.c_long, ctypes.py_object]
ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(0), ctypes.py_object(0))

# The following should not crash
import ctypes
ctypes.
