import gc, weakref

class UncollectableClass:
    def __del__(self):
        print('not collectable!')
        super().__del__()

def weakref_ex():
    """
    Objects are not immediately collected when they go out of scope.
    The reference counter for an object is decremented when it is no
    longer reachable from any reference in the program. This means
    that a program can still access an object through a reference
    even though it is no longer reachable from the program. This can
    be a problem if the object is holding onto a lot of resources.

    A WeakKeyDictionary uses weak references to its keys. If a key
    is no longer reachable, the dictionary entry for it is deleted
    automatically. This is useful for situations where you would
    like to have an object automatically removed from a dictionary
    when it is no longer used elsewhere in the program.

    Weak references are also useful in caches and other places where
    you want to keep a large number of objects around for a short
    time. Weak references allow the cache to discard objects that
    are no longer being used by the program.


