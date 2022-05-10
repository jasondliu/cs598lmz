import weakref
# Test weakref.ref on a class
class X(object):
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        return "<X %s>" % self.a

class Y(object):
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        return "<Y %s>" % self.a

class Z(object):
    def __init__(self, a):
        self.a = a
    def __repr__(self):
        return "<Z %s>" % self.a

def f(a):
    return a

def g(a):
    return a

def h(a):
    return a

def test_call_with_weakrefs(a):
    return a

def test_call_with_weakrefs2(a):
    return a

def test_call_with_weakrefs3(a):
    return a

def test_call_with_weakrefs4(a):
    return a
