import weakref
# Test weakref.ref() argument

class CheckIdentity:
    def __init__(self):
        self.ref = weakref.ref(self)
    def __repr__(self):
        return 'CheckIdentity(%s)' % self.ref() is self

def f():
    pass

CheckIdentity()

c = CheckIdentity()

c = CheckIdentity()
c.ref() is c

c = CheckIdentity()

f()
CheckIdentity()

c = CheckIdentity()

del c

def f():
    CheckIdentity()
f()

CheckIdentity()

