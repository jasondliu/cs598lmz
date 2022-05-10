import weakref
# Test weakref.ref that's ownable.
class C(object):
    pass

w = weakref.ref(C())
# Test weakref.ref that's not ownable.
class D(C):
    _cannot_assemble_as_weakref = True

w = weakref.ref(D())
class BogusError(Exception):

    def __unicode__(self):
        pass

    def __str__(self):
        pass
        return ''.join(chr(i) for i in range(256))
try:
    raise BogusError()
except BogusError:
    pass
else:
    print('Expected an exception!')
try:
    raise BogusError()
except:
    pass
else:
    print('Expected an exception!')
def seqeq(x, y):
    return list(x) == list(y)
# Spec: If a class defines a method __index__()
# it should return an integer.  If not, TypeError.
class A:
    ...

