gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)

# Test gi.gi_frame
print(gi.gi_frame)

# Test gi.gi_running
print(gi.gi_running)

# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)


# Test backref
def gen():
    i = 2
    print(DirSetType(i).toString())
    yield i

gene = gen()
print(DirSetType(gene).toString())
next(gene)
print(DirSetType(gene).toString())

# Test next
print(DirSetType(gene).toString())
gene.gi_frame.f_stacktop = None
print(gene.send(1))

from types import coroutine
from inspect import currentframe

@coroutine
def gen():
    i = 2
    yield i

g = gen()
g.__next__()
print(currentframe())
print(g.send(2), DirSetType(g).toString())

from types
