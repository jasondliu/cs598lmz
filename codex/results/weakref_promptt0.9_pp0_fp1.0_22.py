import weakref
# Test weakref.ref to make sure that it raises a TypeError if its
# first argument is not of a weakly referencable type.

def f(x):
    ref(x)

for x in ['foo', True]:
    raises(TypeError)(f)(x)
