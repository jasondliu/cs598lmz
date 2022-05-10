import weakref
# Test weakref.reference() argument optional.
class A(object):
    pass

a = A()
foo = weakref.reference(a)
a = None
assert foo() is None

# Exercise the line number of the assertion,
# since the line number of the weakref-creation
# line is not being used.
import weakref
try:
    weakref.reference(a)
except NameError:
    import sys
    _, _, tb = sys.exc_info()
    assert tb.tb_lineno == 4
