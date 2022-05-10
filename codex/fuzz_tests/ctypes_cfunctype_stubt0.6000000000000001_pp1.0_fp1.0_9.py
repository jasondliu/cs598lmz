import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_callable():
    assert callable(fun)

def test_call():
    assert callable(fun)
    assert fun() == 1

def test_call_args():
    assert callable(fun)
    assert fun(1) == 1

def test_repr():
    assert repr(fun) == '<cdata ' + repr(FUNTYPE(1)) + ' wrapping <function fun at 0x%x>>' % (id(fun),)

def test_repr_instance():
    class A:
        def __repr__(self):
            return 'hello'
    a = A()
    assert repr(a) == 'hello'

def test_repr_class():
    class A:
        pass
    assert repr(A) == "<class 'A'>"

def test_repr_class_instance():
    class A:
        pass
    a = A()
    assert repr(a) == '<A instance at 0x%x>' % (id(a),)

def test_repr
