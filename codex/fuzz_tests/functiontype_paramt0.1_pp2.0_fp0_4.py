from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that we can use a function as a key in a dict.
d = {}
d[lambda: None] = 1
d[lambda: None]

# Test that we can use a function as a key in a set.
s = set()
s.add(lambda: None)
s.add(lambda: None)

# Test that we can use a function as a key in a frozenset.
fs = frozenset()
fs.add(lambda: None)
fs.add(lambda: None)

# Test that we can use a function as a key in a dict.
d = {}
d[FunctionType(lambda: None, globals(), 'foo')] = 1
d[FunctionType(lambda: None, globals(), 'foo')]

# Test that we can use a function as a key in a set.
s = set()
s.add(FunctionType(lambda: None, globals(), 'foo'))
s.add(FunctionType(lambda: None, globals(), 'foo'))

# Test that we
