import weakref
# Test weakref.ref() on an internal type

class D(object):
    pass

D.__init__(D, 1)
D.x = weakref.ref(D)
print D.x()
print type(D.x)

class C(object):
    def __init__(self):
        self.x = weakref.ref(self)()
print C()
