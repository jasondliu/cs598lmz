import weakref
# Test weakref.ref() and weakref.proxy()

# Create a class with a __del__ method
class C:
    def __del__(self):
        print "C.__del__"

# Create an instance of the class
c = C()

# Create a weak reference to the instance
r = weakref.ref(c)

# Create a weak reference proxy to the instance
p = weakref.proxy(c)

# Print the weak reference and proxy
print "r =", r
print "p =", p

# Delete the instance
del c

# Print the weak reference and proxy
print "r =", r
print "p =", p

# Create a new instance of the class
c = C()

# Print the weak reference and proxy
print "r =", r
print "p =", p

# Create a new weak reference proxy to the instance
p = weakref.proxy(c)

# Print the weak reference and proxy
print "r =", r
print "p =", p

# Delete the instance
del c

# Print the weak reference and proxy
print
