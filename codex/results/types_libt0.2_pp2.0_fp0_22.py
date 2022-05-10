import types
types.MethodType(lambda self: None, None, D)

# Test that __dict__ is a read-only attribute
try:
    D.__dict__ = {}
except TypeError:
    pass
else:
    raise TestFailed, "__dict__ not read-only"

# Test that __dict__ is not there if not explicitly set
class C:
    pass

if hasattr(C, '__dict__'):
    raise TestFailed, "__dict__ present"

# Test that __dict__ is there if set
class C:
    __dict__ = 1

if C.__dict__ != 1:
    raise TestFailed, "__dict__ not set"

# Test that __dict__ is there if inherited
class C(object):
    pass

class D(C):
    pass

if not hasattr(D, '__dict__'):
    raise TestFailed, "__dict__ not inherited"

# Test that __dict__ is there if inherited even if __slots__ are defined
class C(object):
    __slots__ =
