import types
# Test types.FunctionType
a = types.FunctionType(lambda x: x, globals())
# Test types.LambdaType
b = types.LambdaType(lambda x: x, globals())
# Test 'ab'
ab = a + b
# Test 'c'
c = ab(1)
# Test 'd'
d = 'ab'
# Test 'd2'
d2 = 'c = ' + `c`
# Test 'exec'
exec d + '\n' + d2
