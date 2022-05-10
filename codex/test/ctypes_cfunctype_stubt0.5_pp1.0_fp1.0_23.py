import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

def test_function_type():
    assert fun() == 42

def test_method_type():
    class A(object):
        @FUNTYPE
        def fun(self):
            return 42
    a = A()
    assert a.fun() == 42

def test_method_type_in_parent_class():
    class A(object):
        @FUNTYPE
        def fun(self):
            return 42
    class B(A):
        pass
    b = B()
    assert b.fun() == 42

def test_method_type_in_parent_class_overridden():
    class A(object):
        @FUNTYPE
        def fun(self):
            return 42
    class B(A):
        def fun(self):
            return 24
    b = B()
    assert b.fun() == 24

def test_method_type_in_parent_class_overridden_in_parent():
    class A(object):
        def fun(self):
            return 42
