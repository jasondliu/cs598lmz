import weakref
# Test weakref.ref() with a factory function.
class C(object):

    def __init__(self, arg):
        self.arg = arg


def f(arg):
    return C(arg)


o = C(10)
r = weakref.ref(o, f)

def callback(r):
    print(r)
    print(r.arg)


wr = weakref.ref(o, callback)

def f():
    pass
# Test weakref.ref() with a class and factory function.
class C(object):

    def __init__(self, arg):
        self.arg = arg


def f(arg):
    return C(arg)


o = C(10)
r = weakref.ref(o, f)

def callback(arg):
    print(arg)
    print(arg.arg)


wr = weakref.ref(o, callback)

def f():
    pass
# Test weakref.ref() with a lambda function.
