import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    class C(object):
        pass

    c = C()
    return c

def fun_gen():
    class C(object):
        pass

    c = C()
    yield c

def fun_gen2():
    class C(object):
        pass

    c = C()
    yield 0
    yield 1
    yield c

def fun_gen3():
    class C(object):
        pass

    c = C()
    yield 0
    yield 1

def fun_gen4():
    class C(object):
        pass

    c = C()
    yield 1
    yield 0
    yield c

def fun_gen5():
    class C(object):
        pass

    c = C()
    yield 0
    yield 1

def raise_exception():
    class E(Exception):
        pass

    e = E()
    raise e

@jit(error=False)
def use_fun():
    return fun().x

@jit(error=False)
def use_fun_gen(n):
    x = 0
