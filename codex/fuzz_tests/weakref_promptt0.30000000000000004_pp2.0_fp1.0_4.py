import weakref
# Test weakref.ref() with a callable object
#
# This is a test for SF bug #836347.

class Foo:
    def __call__(self):
        return 42

def callback(wr):
    print "callback called"

f = Foo()
wr = weakref.ref(f, callback)
print wr()
del f
print wr()

# Test weakref.ref() with a callable object and a bound method
#
# This is a test for SF bug #836347.

class Foo:
    def __call__(self):
        return 42

def callback(wr):
    print "callback called"

f = Foo()
wr = weakref.ref(f.__call__, callback)
print wr()
del f
print wr()

# Test weakref.ref() with a callable object and a bound method
#
# This is a test for SF bug #836347.

class Foo:
    def __call__(self):
        return 42

def callback(wr):
    print "callback called"

f = Foo()

