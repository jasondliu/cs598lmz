import weakref
# Test weakref.ref for a bug that was fixed in Python 2.4.1
# It used to crash when the referent was a class.
class C(object):
    def __init__(self):
        self.ref = weakref.ref(self)
    def __del__(self):
        self.ref()
c = C()
c.__dict__.keys()

# Test weakref.ref for a bug that was fixed in Python 2.4.1
# It used to crash when the referent was a class.
class C(object):
    def __init__(self):
        self.ref = weakref.ref(self)
    def __del__(self):
        self.ref()
c = C()
c.__dict__.keys()

# Test weakref.ref for a bug that was fixed in Python 2.4.1
# It used to crash when the referent was a class.
class C(object):
    def __init__(self):
        self.ref = weakref.ref(self)
    def __del__(self):
        self.ref()

