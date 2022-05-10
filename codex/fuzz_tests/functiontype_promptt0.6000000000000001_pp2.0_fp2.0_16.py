import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)

# Test in operator
assert not 'a' in 'b'
assert 'b' in ('a', 'b', 'c')
assert 'b' in ['a', 'b', 'c']
assert not 'b' in ['a', 'c']
assert 'b' in {'a': 1, 'b': 2, 'c': 3}
assert not 'b' in {'a': 1, 'c': 3}

# Test list.append
l = [1, 2, 3]
l.append(4)
assert l == [1, 2, 3, 4]
l = []
l.append(1)
assert l == [1]

# Test list.extend
l = [1, 2, 3]
l.extend([4, 5, 6])
assert l == [1, 2, 3, 4, 5, 6]
l = []
l.extend([1, 2
