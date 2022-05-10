import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

def MakePythonCallable(f):
    """
    MakePythonCallable(f) makes a function which can be called from C++.
    The function f will be called on one double argument x and has to
    return a double result.
    """
    pyf = FUNTYPE(f)
    return pyf

def ClassGetter(cls):
    """
    ClassGetter is a wrapper for calling the functions in class cls
    from C++.
    """
    return {'get': cls.Get,
            'set': cls.Set }

class Getter:
    """
    Getter is a wrapper for calling the functions in class cls
    from C++.
    """
    def __init__(self,cls):
        self.cls = cls
    def get(self,name):
        return self.cls.Get(name)
    def set(self,name,value):
        return self.cls.Set(name,value)

class Setter:

