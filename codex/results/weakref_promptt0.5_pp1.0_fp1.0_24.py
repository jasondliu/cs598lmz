import weakref
# Test weakref.ref
class A(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
a = A(10)
d = weakref.ref(a)
print d
a = None
print d()
# Test weakref.WeakKeyDictionary
class B(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
a = B(10)
b = B(20)
d = weakref.WeakKeyDictionary()
d[a] = 'a'
d[b] = 'b'
print d
a = None
print d
# Test weakref.WeakValueDictionary
class C(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
a = C(10)
b = C(20)
d = weakref.WeakValueDictionary()
