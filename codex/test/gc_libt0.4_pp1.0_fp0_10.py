import gc, weakref

class C(object):
    pass

c = C()
c.a = C()
c.a.b = c

def dump_garbage():
    """Show us what's the garbage about"""
