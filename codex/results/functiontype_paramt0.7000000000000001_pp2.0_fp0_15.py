from types import FunctionType
list(FunctionType('''
def f():
    print 42
''', {}).__code__.co_consts)

# - Types

# - Slices
slice(0, 42, 1).start is None
slice(0, 42, 1).stop is None
slice(0, 42, 1).step is None

# - Ellipsis
...

# - Integers
int(1)
int(1,2)
int(1,2,3)
int(1,2,3,4)

# - Floats
float(1)
float(1,2)
float(1,2,3)
float(1,2,3,4)

# - Strings
str(1)
str(1,2)
str(1,2,3)
str(1,2,3,4)

# - Bytes
bytes(1)
bytes(1,2)
bytes(1,2,3)
bytes(1,2,3,4)

# - Unicode
unicode(1)
unicode(1,2)
unicode
