import weakref
# Test weakref.ref()
class TestRef():
    pass

obj = TestRef()
ref = weakref.ref(obj)
print ref.__class__

try:
    weakref.ref(1)
except TypeError, e:
    print type(e), e

del(obj)
print ref()

# Test weakref.proxy()
class TestProxy():
    pass

obj = TestProxy()
p = weakref.proxy(obj)
try:
    p.atata
except ReferenceError, e:
    print type(e), e

try:
    p.unknown_attr = 1
except TypeError, e:
    print type(e), e

del(obj)
try:
    p.atata
except ReferenceError, e:
    print type(e), e


# Test weakref.finalize()

class TestFinalize():
    pass

obj = TestFinalize()

def test_callbck(obj):
    print obj

ref = weakref.finalize(obj, test_callbck, obj)
del obj
