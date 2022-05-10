import weakref
# Test weakref.ref()
import _weakref
assert issubclass(_weakref.ref, weakref.ref)
print('issue #2878 is fixed')

print('passed all tests...')
