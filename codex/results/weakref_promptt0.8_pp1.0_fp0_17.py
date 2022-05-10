import weakref
# Test weakref.ref(allocation_type) doesn't crash, e.g.
#     https://bugs.python.org/issue3365
#     https://bugs.python.org/issue11517
#     https://bugs.python.org/issue27710
#     https://bugs.python.org/issue28066
for cls in (bytearray, list, memoryview, str, tuple, type(None),):
    ref(cls)

del cls
