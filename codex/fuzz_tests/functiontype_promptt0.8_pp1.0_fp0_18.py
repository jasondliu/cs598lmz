import types
# Test types.FunctionType
try:
    t = types.FunctionType
except AttributeError:
    raise ImportError
# test instance method __doc__, __name__ and __class__
def testmethod(self):
    'test function'
    return
class C:
    f = testmethod

# test classic classes
class classic:
    pass

# foo is the new style class we will use to test __class__.
class foo:
    pass

# test __mro__
class A(object): pass
class B(A): pass
class C(A): pass
class D(B,C): pass

# test __bases__
class A(object): pass
class B(A): pass
class C(A): pass
class D(B,C): pass
