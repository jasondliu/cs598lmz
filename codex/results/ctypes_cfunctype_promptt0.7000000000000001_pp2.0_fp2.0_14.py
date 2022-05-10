import ctypes
# Test ctypes.CFUNCTYPE by providing Python implementations of
# functions that take and return pointers to functions.

import _ctypes_test

lib = _ctypes_test.dll

FuncPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def func(arg):
    return arg * 2

# call function with pointer to Python function as parameter
funcptr = FuncPtr(func)
result = lib.ptr_func(funcptr)
if result != funcptr(10):
    raise RuntimeError("ptr_func returned wrong result")

class InvokeCounter(object):
    def __init__(self):
        self.count = 0
    def __call__(self, arg):
        self.count += 1
        return arg

# call function with pointer to Python function as parameter,
# pass the pointer to the Python function back and call it
invoke_counter = InvokeCounter()
funcptr = FuncPtr(invoke_counter)
lib.ptr_func(funcptr)
if invoke_counter.count != 0:
    raise RuntimeError("ptr_
