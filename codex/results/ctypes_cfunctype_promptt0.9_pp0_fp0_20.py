import ctypes
# Test ctypes.CFUNCTYPE for thread safety


class CFuncPtrThread(Thread):
    error_status = 0

    def run(self):
        CFuncPtrThread.error_status |= not RunTests()

PyCFuncPtrType = CFUNCTYPE(c_int, c_int)


def F(x):
    return x+1

f = F
pyf = PyCFuncPtrType(F)

f.__name__ = "F"
f.__module__ = "foo"

pyf.__name__ = "F"
pyf.__module__ = "foo"

ctypes.pythonapi.PyDict_SetItem(ctypes.py_object(locals()),
                                   ctypes.py_object('c_foo'),
                                   ctypes.py_object(CFuncPtrThread))

if __name__ == '__main__':
    for i in range(NUMTHREADS):
        CFuncPtrThread().start()
    for i in range(NUMTHREADS):
        CFuncPtrThread.join()
    if CFuncPtr
