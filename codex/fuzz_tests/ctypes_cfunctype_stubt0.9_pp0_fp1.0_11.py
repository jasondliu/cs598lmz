import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return

def f():
    try:
        fun()
    except Exception as e:
        assert type(e) is TypeError
        print(e)
    else:
        assert 0

f()
print("ok")
"""
First class function()
"""
def f():
    return 123
class A():
    pass

def g():
    a = A()
    a.f = f

    assert a.f() == 123

print("ok")



def g():
    def f():
        def g():
            return 123
        return g
    assert f()() == 123

g()
print("ok")

def f():
    def g():
        return 123
    return g
assert f()() == 123

print("ok")

class A():
    def __eq__(self, other):
        return True

def f():
    a = A()
    b = A()
    assert a == b

f()
print("ok")

def f():
    def g():
        return False
    return g

