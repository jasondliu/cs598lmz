import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World!"

def test_ctypes_py_object():
    f = fun
    assert "Hello World!" == f()
    assert ctypes.py_object == type(f())

def test_ctypes_py_object_method():
    class A(object):
        def f(self):
            return "Hi!"

    a = A()
    f = a.f
    assert "Hi!" == f()
    assert ctypes.py_object == type(f())

def test_ctypes_call_py_object_method():
    class A(object):
        def f(self):
            return "Hi!"

    a = A()
    f = a.f
    assert "Hi!" == ctypes.py_object(f)()
    assert ctypes.py_object == type(ctypes.py_object(f)())

def test_ctypes_call_py_object_method_of_subclass():
    class B(object):
        def f(self):
            return "Hi!"

    class A(B):
       
