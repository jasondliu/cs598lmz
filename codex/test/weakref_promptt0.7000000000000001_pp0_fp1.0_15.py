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

