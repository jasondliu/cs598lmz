import types
types.MethodType(lambda self: 42, list(), list)  # Matches
types.MethodType(lambda self: 42, list(), int)  # Doesn't match

# Using signatures to verify self
@sig(self=int) as defn:
    def f(): pass
def f(): pass  # Matches

@sig(self=int) as defn:
    def f(): pass
def f(self): pass  # Matches

@sig(self=int) as defn:
    def f(): pass
def f(self, x): pass  # Doesn't match


# Using signatures to verify other elements of the method def
sig(self=list, args=[int], ret=int, varargs='x', kwargs='a', kwonlyargs=[True], kwonlydefaults=[False]) as defn:
    def f(): pass
class C:
    __slots__ = (5 + 5, )  # tuple of just ints is okay
    f: defn  # type: ignore

# Test field names
# Each field will have a TestCase in
