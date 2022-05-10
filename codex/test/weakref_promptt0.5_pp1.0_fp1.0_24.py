import weakref
# Test weakref.ref
class A(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)
a = A(10)
d = weakref.ref(a)
