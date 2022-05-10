import weakref
# Test weakref.ref #####################################################################################################
#
# A weakref.ref is a callable that returns the referenced object or None if the object no longer exists.
#
# Weak references are useful for caching large objects, or objects from costly construction methods,
# when memory is tight, and you don’t want to keep them around after they’re no longer needed.
#
# If a cache is used by multiple services it would be a good idea to use weakref since it will not hold
# references to objects that are no longer needed elsewhere in the system, and hence will not prevent them
# from being garbage collected.

def f(x):
    print(x)


def g(x):
    print(x)


class C:
    print('Instantiating C...')
    def __init__(self):
        self.c = 42
        print('C instantiated.')


if __name__ == '__main__':
    foo = C()

    print('Instantiating weak reference to foo...')
    f_ref = weakref.ref(foo, f)

    # Delete the original object
   
