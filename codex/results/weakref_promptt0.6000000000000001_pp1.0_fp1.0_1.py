import weakref
# Test weakref.ref() with a builtin type
import _weakref

class Foo:
    pass

class Bar:
    pass

class Baz:
    pass

def foo():
    pass

def bar():
    pass

def baz():
    pass

obj_list = [
    Foo(),
    Bar(),
    Baz(),
    foo,
    bar,
    baz,
    str,
    int,
    bool,
    dict,
    list,
    tuple,
    set,
    frozenset,
    bytes,
    bytearray,
]

# Create a list of weak references to the objects in obj_list.
ref_list = [weakref.ref(obj) for obj in obj_list]

# Delete the original references to the objects.
del obj_list

# Check that the objects can still be accessed via the weak references.
for i, obj in enumerate(ref_list):
    print(obj(), type(obj()))

# The objects should still be alive.
for ref in ref_list:
    assert ref()
