import types
# Test types.FunctionType = <type 'function'>
# Test types.LambdaType = <type 'function'>

# Test tuple([False, True]) = (False, True)
# Test tuple(x**2 for x in [1, 2, 3]) = (1, 4, 9)
# Test tuple(map(lambda x: x**2, [1, 2, 3])) = (1, 4, 9)
# Test tuple('abc') = ('a', 'b', 'c')

# Test list([False, True]) = [False, True]
# Test list(x**2 for x in [1, 2, 3]) = [1, 4, 9]
# Test list(map(lambda x: x**2, [1, 2, 3])) = [1, 4, 9]
# Test list('abc') = ['a', 'b', 'c']

# Test dict([[1, 2], [3, 4]]) = {1: 2, 3: 4}
# Test dict(1=2, 3=4) = {1: 2, 3: 4}

# Test set([
