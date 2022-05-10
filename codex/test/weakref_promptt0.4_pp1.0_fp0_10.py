import weakref
# Test weakref.ref(self) in __del__ method.

class C:
    def __init__(self):
        self.ref = weakref.ref(self)
    def __del__(self):
        self.ref()

c = C()
c.__dict__
c.__dict__['ref']()
c.__dict__['ref'].__class__
c.__dict__['ref'].__class__.__name__
c.__dict__['ref'].__class__.__module__
c.__dict__['ref'].__class__.__module__.__class__
c.__dict__['ref'].__class__.__module__.__class__.__name__
c.__dict__['ref'].__class__.__module__.__class__.__module__
c.__dict__['ref'].__class__.__module__.__class__.__module__.__class__
c.__dict__['ref'].__class__.__module__.__class__.__module__.__class__.__name__
c
