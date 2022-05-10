import weakref
# Test weakref.ref

# Create a class to use as a key
class C:
    pass

# Create a weak reference to a key
r = weakref.ref(C)

# Create a weak reference to an object
o = C()
p = weakref.ref(o)

# Show that the weak references are dead
print 'r():', r()
print 'p():', p()

# Delete the original references
del C, o

# Show that the weak references are dead
print 'r():', r()
print 'p():', p()

# Show that the weak references are equal
print 'r is p:', r is p

# Create a weak reference to another object
o = C()
q = weakref.ref(o)

# Show that the weak references are not equal
print 'p is q:', p is q

# Show that the weak references are dead
print 'r():', r()
print 'p():', p()
print 'q():', q()

# Show that the weak reference to the key is dead
print 'r is q:', r is q


