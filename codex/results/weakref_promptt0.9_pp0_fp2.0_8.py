import weakref
# Test weakref.ref(failobj=42)
w = weakref.ref({}, failobj=42)
print(w(), 42)
# Test weakref.ref(callback=None)
w = weakref.ref({}, callback=None)
print(w(), None)
# Test strong ref cache
a = []
w = weakref.ref(a)
a.append(1)
print(w(), [1])
w = weakref.ref({})
print(w(), {})
# Test Custom class with weakrefable
class C(tuple): pass
w = weakref.ref(C((1, 2)))
print(w(), (1, 2))
# Test freeing ref when object is deallocated
ref = lambda: None  # LoopingClosure with freevars, hence not WeakrefClosure
a = []
ref.w = weakref.ref(a, lambda _: print(_ == a, True, "weakly referenced object got deleted"))
del a
# check error conditions
# KeyError can also be nested an arbitrary number of times.
# test that the cleanup function cannot override the weak reference
def cleanup(
