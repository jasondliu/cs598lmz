import weakref
# Test weakref.ref and weakref.WeakSet for success or failure.

class Foo:
    pass

foo1 = Foo()
foo2 = Foo()

if verbose:
    print "Testing weakref.ref"

if verbose:
    print "\nCreating weak reference to foo1"
weak_foo1 = weakref.ref(foo1)
if weak_foo1() is not None:
    if verbose:
        print "\nfoo1 was not weakly referenced"
    raise TestError

if verbose:
    print "\nDeleting foo1"
del foo1

if weak_foo1() is not None:
    if verbose:
        print "\nfoo1 was not weakly referenced"
    raise TestError

if verbose:
    print "\nCreating weak reference to foo2"
weak_foo2 = weakref.ref(foo2)

if weak_foo2() is not foo2:
    if verbose:
        print "\nfoo2 was weakly referenced"
    raise TestError

if verbose:
    print "\nDeleting weak
