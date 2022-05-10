import weakref
# Test weakref.ref()

# The 'ref' argument is required.
try: weakref.ref()
except TypeError: pass
else: print('FAILED: weakref.ref() with no arguments')

# The 'ref' argument must be callable.
try: weakref.ref([])
except TypeError: pass
else: print('FAILED: weakref.ref() for non-callable')

# The 'ref' argument should return a non-negative integer.
try: weakref.ref(lambda: "foo")
except TypeError: pass
else: print('FAILED: weakref.ref() for non-number')

# The 'ref' argument may return a floating point number - it is truncated.
try:
    x = weakref.ref(lambda: 3.14)
    if x() != 3:
        print('FAILED: weakref.ref() for float')
except TypeError:
    print('FAILED: weakref.ref() for float')

# The 'ref' argument may return a very large integer - it is truncated.
