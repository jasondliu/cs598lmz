import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.py_object, ctypes.py_object, ctypes.py_object)

def py_callback(cfun, pyfun):
    cb = FUNTYPE(pyfun)
    cfun.contents.py_callback = cb

def py_callback_on_raise(cfun, pyfun):
    cb = FUNTYPE(pyfun)
    cfun.contents.py_callback_on_raise = cb

def py_callback_on_except(cfun, pyfun):
    cb = FUNTYPE(pyfun)
    cfun.contents.py_callback_on_except = cb

def py_callback_on_finally(cfun, pyfun):
    cb = FUNTYPE(pyfun)
    cfun.contents.py_callback_on_finally = cb

def py_callback_on_leave(cfun, pyfun):
    cb = FUNTYPE(pyfun)
    cfun.contents.py_callback_on_leave = cb

def py_callback_user
