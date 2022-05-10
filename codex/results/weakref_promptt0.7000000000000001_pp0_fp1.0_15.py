import weakref
# Test weakref.ref() on a class that overrides __del__.
#
# The intended behavior of weakref.ref() is that __del__ methods
# should be called when the weakref.ref() goes out of scope, as
# long as there are no other references to the object.
#
# In this test, we create a class, Bar, with an overridden __del__
# method, and a weakref.ref() to it.  If the weakref.ref() is the
# last reference to the object, and the weakref.ref() goes out of
# scope, we expect the __del__ method to be called.

class Bar:
    def __init__(self, id):
        print "__init__ called with id = ", id
        self.id = id

    def __del__(self):
        print "__del__ called with id = ", self.id

def create_and_destroy():
    print ""
    print "Creating Bar(1), and a weak reference to it"
    b = Bar(1)
    b_ref = weakref.ref(b)
    print "b
