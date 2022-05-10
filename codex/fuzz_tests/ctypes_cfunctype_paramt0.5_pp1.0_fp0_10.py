import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)

class MyFunction(object):
    def __init__(self, function):
        self.function = function
    def __call__(self, *args):
        return self.function(*args)
    def __reduce__(self):
        return (_wrap_function, (self.function,))

def _wrap_function(function):
    return MyFunction, (function,)

def _unwrap_function(func_object, args):
    return func_object.function(*args)

class MyFunction2(object):
    def __init__(self, function):
        self.function = function
        self.func_object = FUNTYPE(function)
    def __call__(self, *args):
        return self.function(*args)
    def __reduce__(self):
        return (_wrap_function2, (self.function,))

def _wrap_function2(function):
    obj = MyFunction2(function)
    return obj, (obj.func_object,)

def _unwrap
