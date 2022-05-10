import weakref
# Test weakref.ref(class)
class A:
    pass

def make_ref():
    return weakref.ref(A)

def make_ref_to_instance():
    return weakref.ref(A())

class B(weakref.ref):
    pass

def make_ref_to_instance():
    return B(A())
