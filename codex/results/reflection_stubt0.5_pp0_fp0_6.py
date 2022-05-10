fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# getattr
getattr(gi, '__code__')

# hasattr
hasattr(gi, '__code__')

# hash
hash(gi)

# hex
hex(1)

# id
id(gi)

# input
input('?')

# isinstance
isinstance(gi, GeneratorType)

# issubclass
issubclass(type(gi), GeneratorType)

# iter
iter(gi)

# len
len(gi)

# locals
locals()

# map
map(lambda x: x, gi)

# max
max(gi)

# min
min(gi)

# next
next(gi)

# oct
oct(1)

# open
open('/dev/null')

# ord
ord('a')

# pow
pow(1, 2)

# print
print('gi')

# property
class Property(object):
    def __init__(self, fget=None, fset=None, fdel
