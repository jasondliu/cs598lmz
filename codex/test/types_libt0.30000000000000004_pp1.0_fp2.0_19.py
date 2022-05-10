import types
types.MethodType(lambda self, x: x, None)

# Test that the __class__ descriptor works
class C:
    pass
class D(C):
    def __get__(self, obj, type=None):
        return type
assert C().__class__ is C
assert D().__class__ is C
assert C.__class__ is type
assert D.__class__ is type

# Test that the __class__ descriptor works with subclasses of 'object'
class C(object):
    pass
class D(C):
    def __get__(self, obj, type=None):
        return type
assert C().__class__ is C
assert D().__class__ is C
assert C.__class__ is type
assert D.__class__ is type

# Test that the __class__ descriptor works with metaclasses
class C(type):
    pass
class D(C):
    def __get__(self, obj, type=None):
        return type
assert C().__class__ is C
assert D().__class__ is C
assert C.__class__ is type
