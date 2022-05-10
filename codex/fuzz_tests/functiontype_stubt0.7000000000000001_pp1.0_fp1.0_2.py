from types import FunctionType
a = (x for x in [1])
b = ((y for y in [2]), (z for z in [3]),)
c = (((a for a in [4]), (b for b in [5])), (c for c in [6]))
d = (((a for a in [7]), ((b for b in [8]), (c for c in [9]))), ((d for d in [10]), (e for e in [11])))

assert isinstance(a, GeneratorType)
assert not isinstance(a, FunctionType)
assert not isinstance(a, tuple)

assert isinstance(b, tuple)
assert not isinstance(b, GeneratorType)
assert not isinstance(b, FunctionType)
assert len(b) == 2
assert isinstance(b[0], GeneratorType)
assert isinstance(b[1], GeneratorType)

assert isinstance(c, tuple)
assert not isinstance(c, GeneratorType)
assert not isinstance(c, FunctionType)
assert len(c) == 2
assert isinstance(c[0], tuple)
assert isinstance(c[1], GeneratorType
