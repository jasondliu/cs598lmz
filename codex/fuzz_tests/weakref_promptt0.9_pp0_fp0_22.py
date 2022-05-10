import weakref
# Test weakref.ref() under exception conditions.
print 'Testing ref() with invalid objects:'
try:
    r = weakref.ref(1)
except TypeError:
    pass
else:
    print '    expected TypeError'

try:
    r = weakref.ref(A())
except TypeError:
    pass
else:
    print '    expected TypeError'
print '    no garbage after failed calls to ref()'
print '    (if the second call results in a TypeError, there may be garbage)'
print gc.collect()
print ''
#

class GetReturnsInvalid(object):

    def __init__(self):
        self.__dict__['foo'] = None


class CallReturnsInvalid(object):

    def __call__(self):
        pass


def set_and_get_returns_invalid(cls):
    try:
        ref = weakref.ref(cls())
        try:
            ref()
        except TypeError:
            pass
        else:
            raise AssertionError('expected a TypeError')

        try:
            ref
