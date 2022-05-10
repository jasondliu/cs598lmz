import ctypes
ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id), ctypes.py_object(SystemExit))
</code>
Btw, this was inspired by this answer.

