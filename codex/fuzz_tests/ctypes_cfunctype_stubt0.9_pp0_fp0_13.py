import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return thread.allocate_lock()
dll = loadlibrary.load_library("foo", "test/ctypes_issue20562/build")
dll.globalVar.setter(fun)
