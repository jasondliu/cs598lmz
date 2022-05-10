fn = lambda: None
# Test fn.__code__ is read-only
try:
    fn.__code__ = 1
except:
    passed = True
assert passed

# Test fn.__code__ new-style
class C(object):
    def fn(self):
        pass

try:
    fn.__code__ = 1
except:
    passed = True
assert passed
