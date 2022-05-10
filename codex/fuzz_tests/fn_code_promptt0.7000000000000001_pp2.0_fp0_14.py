fn = lambda: None
# Test fn.__code__.co_argcount

class A(object):
    def f0(self): pass
    def f1(self, a): pass
    def f2(self, a, b): pass
    def f3(self, a, b, c): pass
    def f4(self, a, b, c, d): pass
    def f5(self, a, b, c, d, e): pass
    def f6(self, a, b, c, d, e, f): pass
    def f7(self, a, b, c, d, e, f, g): pass
    def f8(self, a, b, c, d, e, f, g, h): pass
    def f9(self, a, b, c, d, e, f, g, h, i): pass
    def f10(self, a, b, c, d, e, f, g, h, i, j): pass
    def f11(self, a, b, c, d, e, f, g, h, i, j, k): pass
    def
