fn = lambda: None
# Test fn.__code__
class Foo:
    def __init__(self):
        code_fn = self.__code__
        self.foo()
    def foo(self): pass
    def cmp(self, other): return cmp(self.__code__, other.__code__)
class Bar:
    # __code__ needs to be explicitly set to something else
    __code__ = None
    def __init__(self):
        code_fn = self.__code__
        self.foo()
    def foo(self): pass
    def cmp(self, other): return cmp(self.__code__, other.__code__)

f = Foo()
print f.__code__
b = Bar()
try: print b.__code__
except AttributeError, e: print e
print cmp(f.__code__, Foo.__code__), cmp(f.__code__, f.cmp.__code__)
print cmp(Foo.__code__, f.cmp.__code__), cmp(Foo.__code__, Bar.__code__
