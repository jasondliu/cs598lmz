import weakref
# Test weakref.ref() on a str
import _weakref

class MyStr(str):
    pass

s = MyStr('test')
# The following tests that the type check for the type of the
# referent is done by identity, not by comparing the names of the
# types.  That is, s is not simply an instance of the type str,
# but specifically an instance of MyStr.  Thus, the type check in
# the weakref.ref call will fail unless it is done by identity.
r = weakref.ref(s)
print('str(r) is', repr(str(r)))
print('r() is', repr(r()))

if r() is not s:
    print('r() is not s')
    raise Exception

if r() != s:
    print('r() != s')
    raise Exception

if type(r()) is not type(s):
    print('type(r()) is not type(s)')
    raise Exception

print('s is', repr(s))
del s
print(repr(r()))
if r() is not None
