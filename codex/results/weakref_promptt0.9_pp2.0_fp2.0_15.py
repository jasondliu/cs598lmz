import weakref
# Test weakref.ref and weakref.proxy.
# Tests of the predicates weakref.ref() and weakref.proxy()
# not included because they are implicitly tested below.

x = "Hello"


class A:

    def goodbye(self):
        return 'Goodbye'


a = A()
x_ref = weakref.ref(x)
a_ref = weakref.ref(a)

# Testing that a weakref to a string works
if x_ref() != x:
    raise AssertionError

# Testing that a weakref to an instance works
if a_ref() != a:
    raise AssertionError

# Testing that the weakrefs do not hold the references
refs = []
for i in range(1, 100):
    refs.append(weakref.ref(a))
del refs
try:
    a_ref()
except ReferenceError:
    pass
else:
    raise AssertionError

# Testing that the weakrefs do not hold the references
refs = []
for i in range(100):
    refs.append(
