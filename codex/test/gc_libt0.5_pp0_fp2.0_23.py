import gc, weakref

def get_refcounts(objects):
    return dict([(id(o), sys.getrefcount(o)) for o in objects])

class A:
    pass

a = A()
b = A()

a_id = id(a)
b_id = id(b)

