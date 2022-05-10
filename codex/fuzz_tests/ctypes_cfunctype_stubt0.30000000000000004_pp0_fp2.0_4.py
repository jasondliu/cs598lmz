import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

class Foo:
    def __init__(self):
        self.x = 42
    def meth(self):
        return self.x

def test_meth():
    foo = Foo()
    assert foo.meth() == 42

def test_meth_call():
    foo = Foo()
    assert foo.meth.__call__() == 42

def test_meth_call_arg():
    foo = Foo()
    assert foo.meth.__call__(foo) == 42

def test_meth_call_arg2():
    foo = Foo()
    assert foo.meth.__call__(foo, foo) == 42

def test_meth_call_arg3():
    foo = Foo()
    assert foo.meth.__call__(foo, foo, foo) == 42

def test_meth_call_arg4():
    foo = Foo()
    assert foo.meth.__call__(foo, foo, foo
