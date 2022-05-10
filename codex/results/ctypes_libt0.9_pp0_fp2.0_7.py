import ctypes
ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(Long(thread.ident)), ctypes.py_object(SystemExit))
</code>
Since its using Python C API, it seems like it can't be done with other language.

