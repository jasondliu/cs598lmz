import weakref
# Test weakref.ref
# from weakref import ref
class klass:
    pass
inst = klass()
r = weakref.ref(inst)
