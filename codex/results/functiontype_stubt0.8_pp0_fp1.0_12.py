from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
d = (x for x in [1,2])
c = (x for x in [1])
assert a == b
assert a != c
assert a != d
assert d != 1
assert a != 1
assert a != {}
assert a != []
assert a != [[[[[[[]]]]]]]
assert a != ((1,2),2,3)
assert a != {1,2,3}
assert a != dict(a=1,b=2)

assert 1 == 1
assert 1 != 2
assert 1 != 'a'
assert 'a' != 1
assert 'a' == 'a'
assert 'a' != 'b'
assert 'a' != 'ab'
assert 'a' != 1

assert dict(a=1) == dict(a=1)
assert dict(a=1) != dict(a=2)
assert dict(a=1) != dict(a=1,b=2)
assert dict(a=1) != dict(b=1)
assert dict(a=1) != dict(
