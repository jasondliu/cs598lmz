import weakref
# Test weakref.ref() with some of the basic types.

# Check that weak references work with int
print 'Testing weak reference with int'
x = 1
r = weakref.ref(x)
print 'x:', x
print 'r():', r()
x = 2
print 'x:', x
print 'r():', r()

# Check that weak references work with long
print 'Testing weak reference with long'
x = 1L
r = weakref.ref(x)
print 'x:', x
print 'r():', r()
x = 2L
print 'x:', x
print 'r():', r()

# Check that weak references work with float
print 'Testing weak reference with float'
x = 1.0
r = weakref.ref(x)
print 'x:', x
print 'r():', r()
x = 2.0
print 'x:', x
print 'r():', r()

# Check that weak references work with complex
print 'Testing weak reference with complex'
x = 1e20+1j
r = weakref.ref(x)
print
