import weakref
# Test weakref.ref() and weakref.proxy()

class D:
    pass

class C:
    pass

class B(C):
    pass

class A(B, D):
    pass

