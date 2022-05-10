import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    x = fun

    class C(object):
        def __call__(self):
            return x
    return C()
res = fun()()
print repr(res), repr(res())

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(x):
    y = fun
    class C(object):
        def __call__(self, z):
            return y
    return C()
res = fun(None)
print repr(res), repr(res(None))

@FUNTYPE
def fun(x):
    '<unprintable function object>'
    class C(object):
        def __call__(self, y):
            return x
    y = fun
    return C()


res = fun(None)
print res, res.func_doc
print repr(res), repr(res(None))
res = fun(1)
print repr(res), repr(res(None))
res = fun(fun)
print repr(res), repr(res(None))
