import weakref
# Test weakref.ref() with objects of various types

def f(x):
    print('f()')

def g():
    print('g()')

def h(x, y):
    print('h()')

def t1():
    # Test weakref.ref() with objects of various types
    objects = [None,
               42,
               2**100,
               2**1000,
               3.14,
               1j,
               'a string',
               u'a unicode string \u1234',
               (),
               (1, 2, 3),
               [],
               [1, 2, 3],
               {},
               {'one': 1, 'two': 2, 'three': 3},
               set(),
               frozenset(),
               f,
               weakref.ref(f),
               weakref.ref(f),
               weakref.ref(g),
               weakref.ref(g),
               weakref.ref(h, 1),
               weakref.ref(h, 1),
               weakref.ref(h, 2),
               weakref
