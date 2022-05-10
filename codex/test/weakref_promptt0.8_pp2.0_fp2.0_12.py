import weakref
# Test weakref.ref()
import weakref, gc
class MyObj:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<MyObj({})>'.format(self.name)
a = MyObj('a')      # Create a reference
b = MyObj('b')      # Create another reference
r = weakref.ref(a)  # Create a weak reference to a
print(r)            # Show the weak reference
print(r())          # Show the referenced object
del a               # Delete the reference
print(r())          # The weak reference still exists
print(r() is None)  # Show whether it's live
b = None            # Delete another reference to the same object
gc.collect()        # Force garbage collection
print(r() is None)  # Now the weak reference is dead
print()

# Test weakref.getweakrefcount() and weakref.getweakrefs()
import weakref
# Create a couple of objects to be referenced
class MyObj:
    def __init__(self, name):
        self
