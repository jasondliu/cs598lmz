import types
# Test types.FunctionType
assert type(lambda: 0) == types.FunctionType

# Test built-in functions
# (https://docs.python.org/3.8/library/functions.html)
assert any((0,)) is False
assert any((0, 1)) is True
assert ascii(None) == 'None'
assert bin(0b1) == '0b1'
assert bool([]) is False
assert bool([0]) is True
assert chr(65) == 'A'
assert complex(2, -3) == (2 - 3j)
assert divmod(8, 3) == (2, 2)
assert enumerate('abc') == [(0, 'a'), (1, 'b'), (2, 'c')]
assert eval('2*3') == 6
assert filter(lambda x: x % 2 == 0, (1, 2, 3)) == [2]
assert float(2) == 2.0
assert format(1.2345, '>10') == '    1.2345'
assert frozenset([1, 2, 3]) == frozenset([1
