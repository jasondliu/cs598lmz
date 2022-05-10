from types import FunctionType
list(FunctionType(compile("", "", "exec"), {}, "") for i in range(2))

# PyPy doesn't support __sizeof__ yet
#assert list.__sizeof__() == 56

l = list(range(3))
assert l.__sizeof__() == 72

assert len(l) == 3
assert repr(l) == "[0, 1, 2]"

# list.__add__()
l = [1, 2]
assert l.__add__([3]) == [1, 2, 3]
assert l == [1, 2]

# list.__contains__()
assert 1 in l
assert 3 not in l

# list.__delitem__()
l = [1, 2, 3]
del l[1]
assert l == [1, 3]

try:
    del l[42]
except IndexError:
    pass
else:
    assert False, "didn't raise IndexError"

# list.__delslice__()
l = [1, 2, 3, 4, 5]
del l[1:
