import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def f():
    return fun()

def g():
    return f()

def h():
    return g()

def test_func():
    res = h()
    print(res)

test_func()
</code>
Note that this is a very contrived example. I am aware that I can simply <code>return fun()</code> from <code>h()</code>.

