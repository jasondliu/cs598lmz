import gc, weakref


class WeakMethod(object):
    def __init__(self, obj, method):
        self.obj = weakref.ref(obj)
        self.method = method

    def __call__(self, *args, **kwargs):
        obj = self.obj()
        if obj is None:
            return

        return getattr(obj, self.method)(*args, **kwargs)


class WeakMethodType(type):
    def __get__(self, obj, objtype):
        return WeakMethod(obj, self.method)


class WeakMethod(object):
    __metaclass__ = WeakMethodType
    method = None


class A(object):
    def __init__(self):
        self.b = B(self)

    def foo(self):
        print "foo"


class B(object):
    def __init__(self, a):
        self.a = a

    def bar(self):
        print "bar"


if __name__ == "__main__":
    a = A()
    a.foo()

