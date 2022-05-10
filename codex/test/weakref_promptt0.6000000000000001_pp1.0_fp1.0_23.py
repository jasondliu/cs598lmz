import weakref
# Test weakref.ref(self) within a class.

class A:
    def __init__(self):
        self.b = weakref.ref(self)

