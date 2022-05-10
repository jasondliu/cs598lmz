import weakref
# Test weakref.ref()
def foo( a ):
    print "foo", a

x = foo
y = weakref.ref( x, foo )
print "x=", x
print "y=", y
print "y()=", y()
print "x is y()", x is y()

x = 1
print "x=", x
print "y=", y
print "y()=", y()
