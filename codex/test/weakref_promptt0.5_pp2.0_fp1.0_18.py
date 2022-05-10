import weakref
# Test weakref.ref() with a class that has a custom __del__() method.

class A(object):
    def __init__(self):
        self.ref = weakref.ref(self)
    def __del__(self):
        self.ref()

a = A()
a.ref()
del a
# Test weakref.WeakValueDictionary() with a class that has a custom __del__() method.

class A(object):
    def __init__(self):
        self.ref = weakref.WeakValueDictionary()
        self.ref[1] = self
    def __del__(self):
        self.ref[2] = self

a = A()
a.ref[3] = a
del a
# Test weakref.WeakValueDictionary() with a class that has a custom __del__() method.

class A(object):
    def __init__(self):
        self.ref = weakref.WeakValueDictionary()
        self.ref[1] = self
