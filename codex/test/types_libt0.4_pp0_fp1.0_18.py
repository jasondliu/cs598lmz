import types
types.new_class('A', (object,), {'method': lambda self: self})

class B(object):
    def method(self):
        return self

class C(object):
    pass

class D(object):
    def __init__(self):
        self.method = lambda self: self

class E(object):
    def method(self):
        return self

def f():
    return lambda self: self

E.method = f()

class F(object):
    def __init__(self):
        self.method = f()

class G(object):
    def __init__(self):
        self.method = lambda self: self

class H(object):
    pass

H.method = lambda self: self

class I(object):
    def __init__(self):
        pass

I.method = lambda self: self

class J(object):
    def __init__(self):
        self.method = lambda self: self

def k():
    return lambda self: self

J.method = k
