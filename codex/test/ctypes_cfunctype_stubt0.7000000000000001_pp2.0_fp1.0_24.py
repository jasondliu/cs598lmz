import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

@FUNTYPE
def fun2(n):
    if n == 0:
        return "Hello"
    else:
        return "World"

@FUNTYPE
def fun3(i, j):
    return i + j

@FUNTYPE
def fun4(i, j, k):
    return i + j + k


@FUNTYPE
def fun5(i, j, k, l):
    return i + j + k + l

def test_0():
    gil = pyjitpl.get_GIL()
    gil.set_param(0)
    assert gil.do_call(fun) == "Hello"

def test_1():
    gil = pyjitpl.get_GIL()
    gil.set_param(0)
    assert gil.do_call(fun2) == "Hello"
    gil.set_param(1)
    assert gil.do_call(fun2) == "World"

def test_2():
    gil = pyjitpl.get_
