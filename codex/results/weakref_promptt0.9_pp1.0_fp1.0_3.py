import weakref
# Test weakref.ref() on new-style classes inheriting from object and
# old-style classes (not inheriting from object).

import weakref

class D(object):
    pass

class E:
    pass

for C in D, E:
    o = C()
    ref = weakref.ref(o)
    assert ref() is o
    assert type(o) is type(ref())
    assert type(o) is C
    assert type(ref()) is C
    del o
    assert ref() is None

# Other test cases in test_descr.py
