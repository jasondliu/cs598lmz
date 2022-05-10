import types
types.MethodType(lambda self, x: 42, None, cls)

# Test that if we have a __class__ attribute, we don't
# accidentally return it.
class C(object):
    def __init__(self):
        self.__class__ = 42

assert C().__class__ == C

# Test that we don't accidentally return the __class__ attribute
# when doing a lookup on a type.
class C(object):
    pass
C.__class__ = 42
assert C.__class__ == type

# Test that we don't accidentally return the __class__ attribute
# when doing a lookup on a type.
class C(object):
    pass
C.__class__ = 42
assert C.__class__ == type

# Test that we don't accidentally return the __class__ attribute
# when doing a lookup on a type.
class C(object):
    pass
C.__class__ = 42
assert C.__class__ == type

# Test that we don't accidentally return the __class__ attribute
# when doing a lookup on a type.
