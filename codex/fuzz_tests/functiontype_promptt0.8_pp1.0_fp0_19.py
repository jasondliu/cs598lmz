import types
# Test types.FunctionType

def sqr( x ): return x * x

def foo( a, x):
	return eval(a, {}, {'x':x, 'sqr':sqr})

assert foo('x', 3) == 3
assert foo('sqr(x)', 3) == 9
assert foo('2*sqr(x)+x', 3) == 15
