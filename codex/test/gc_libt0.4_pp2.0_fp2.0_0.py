import gc, weakref

class A(object):
    def __init__(self):
        self.b = B()
        self.c = C()

class B(object):
    def __init__(self):
        self.a = A()

class C(object):
    def __init__(self):
        self.a = A()

