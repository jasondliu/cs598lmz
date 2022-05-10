import weakref
# Test weakref.ref(file)

# Create the file object we want to test
import support
file = support.make_empty_file("test264.dat")

def test(file):
    # Create a weak reference to the file object
    ref = weakref.ref(file)
    del file

    # See if we can still get the file object from the weak reference
    if ref() is None:
        raise support.TestError("Wrong behaviour of weak reference")

test(file)
# Do it again, to make sure that the original can be destroyed
test(file)
del file

# Make sure the weakref module doesn't crash when the target is GC'ed
# before the ref is used.
import weakref
class A:
    pass
a = A()
a.x = weakref.ref(A())
a = None
# Make sure the weakref module doesn't crash when the target is GC'ed
# after the ref is used.
import weakref
class A:
    pass
a = A()
a.x = weakref.ref(A())
a.x()
