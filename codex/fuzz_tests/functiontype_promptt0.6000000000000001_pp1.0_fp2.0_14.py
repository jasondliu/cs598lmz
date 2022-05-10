import types
# Test types.FunctionType
class A(object):
    def __init__(self):
        pass
    def f(self):
        print "f"

print type(A.f)
print type(A)
print type(A())
print type(A.__init__)
print type(A.__init__.im_self)
print type(A.__init__.im_func)
print type(A.__init__.__get__(A()))

a = A()
print type(a.__dict__)
print type(a.f)
print type(a.f.im_self)
print type(a.f.im_func)
print type(a.f.__get__(a))
print type(a.f.__get__(a).im_self)
print type(a.f.__get__(a).im_func)

print type(A.__dict__)
print type(A.f.__get__(a).__dict__)
print type(a.__dict__)

# Test types.GeneratorType
def
