import gc, weakref


class Object(object):
    def __init__(self):
        self.value = 'value'
    def __del__(self):
        print 'del'

def reference_cycle():
    a = Object()
    b = Object()
    a.other = b
    b.other = a

def reference_chain():
    a = Object()
    b = Object()
    c = Object()
    d = Object()
    a.other = b
    b.other = c
    c.other = d
    d.other = a

def reference_count():
    a = Object()
    b = Object()
    c = a
    print 'count:', sys.getrefcount(a)
    a.other = b
    print 'count:', sys.getrefcount(a)
    a = None
    print 'count:', sys.getrefcount(b)
    b.other = None
    print 'count:', sys.getrefcount(b)

def weak_reference():
    a = Object()
    b = Object()

