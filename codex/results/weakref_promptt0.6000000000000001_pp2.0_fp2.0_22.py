import weakref
# Test weakref.ref() and weakref.proxy()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%r)' % self.name

class Bar(object):
    def __init__(self, obj):
        self.obj = obj
    def __repr__(self):
        return 'Bar(%r)' % self.obj

class Callable(object):
    def __init__(self, obj):
        self.obj = obj
    def __call__(self):
        return self.obj
    def __repr__(self):
        return 'Callable(%r)' % self.obj

class Weak(object):
    def __init__(self, obj):
        self.obj = weakref.ref(obj)
    def __call__(self):
        return self.obj()
    def __repr__(self):
        return 'Weak(%r)' % self.obj()

class WeakProxy(object):
    def __init__(
