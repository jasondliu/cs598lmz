import weakref
# Test weakref.ref

# Define a function that takes an object as argument, and returns a
# weak reference to it.
def ref(obj):
    return weakref.ref(obj)

# Define a function that takes a weak reference as argument, and returns
# the referent if the weak reference is live.
def deref(obj):
    return obj()

# Define a function that takes an object as argument, and returns a
# weak reference to it, along with a list containing the object.
def ref_and_list(obj):
    lst = [obj]
    return weakref.ref(obj), lst

# Define a function that takes a weak reference as argument, and returns
# the referent if the weak reference is live, along with a list
# containing the object.
def deref_and_list(obj):
    return obj(), obj.__self__

# Define a function that takes an object as argument, and returns a
# weak reference to it, along with a list containing the object.
def ref_and_list_global(obj):
    global lst
    l
