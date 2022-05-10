import weakref
# Test weakref.ref() with a class that overrides __del__.
# This was broken in Python 2.2.1.

class C(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print "del", self.name

class D(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print "del", self.name
        raise RuntimeError

class E(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print "del", self.name
        raise ValueError

class F(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print "del", self.name
        raise SystemError

class G(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print "del", self.name

