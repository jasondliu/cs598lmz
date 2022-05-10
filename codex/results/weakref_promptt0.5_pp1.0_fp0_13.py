import weakref
# Test weakref.ref() on a subclass of a builtin type.

class MyInt(int):
    pass

class MyStr(str):
    pass

class MyTuple(tuple):
    pass

class MyList(list):
    pass

class MyDict(dict):
    pass

class MySet(set):
    pass

class MyFrozenset(frozenset):
    pass

class MyObject(object):
    pass

def test_weakref_on_subclass_of_builtin_type():
    for base in (MyInt, MyStr, MyTuple, MyList, MyDict, MySet, MyFrozenset, MyObject):
        # Create an instance of the subclass and a weak reference to it.
        instance = base()
        ref = weakref.ref(instance)
        # Check that the weak reference references the instance.
        assert ref() is instance
        # Check that the weak reference is of the correct type.
        assert isinstance(ref, weakref.ReferenceType)
        assert type(ref) == weakref.ReferenceType
