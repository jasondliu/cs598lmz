import gc, weakref

class C(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'C(%s)' % self.name

def f(x):
    print 'f(%s)' % x

class WeakMethod(object):
    def __init__(self, func):
        self.func = func
        self.instance = None
        self.weakref = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            raise TypeError("Method called on dead object")
        return self.func(self.instance, *args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        self.instance = instance
        self.weakref = weakref.ref(instance)
        return self

class WeakMethod2(object):
    def __init__(self, func):
        self.func = func
        self.instance = None
        self.weakref = None

   
