import weakref
# Test weakref.ref on a builtin type
import sys

def f():
    print 2

r = weakref.ref(f, f)

if r() is not f:
    print 'failed'
    sys.exit(1)

print 'passed'
