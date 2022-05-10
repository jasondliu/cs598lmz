import weakref
# Test weakref.ref
class B(object):
    def __init__(self):
        self.x = 42

class C(object):
    def __init__(self):
        self.b = B()

class D(object):
    def __init__(self):
        self.c = C()

