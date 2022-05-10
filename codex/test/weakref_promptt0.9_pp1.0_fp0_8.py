import weakref
# Test weakref.ref() when the object is deleted before the end of the
# weakref.ref() call.
class Boo:
    pass

