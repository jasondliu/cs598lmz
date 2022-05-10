import types
# Test types.FunctionType
def hamm(x, y, z):
	return x*y*z
def norm(vec):
	n = 0
	for x in vec:
		n += x*x
	return sqrt(n)

a = types.FunctionType(hamm.__code__, globals(), 'norm', hamm.__defaults__, hamm.__closure__)
a.__code__
assert a(1, 2, 3) == 6

b = types.FunctionType(norm.__code__, globals(), 'norm', norm.__defaults__, norm.__closure__)
assert b([1,2,3,4]) == 5.47

# copy shallow copy
import copy
a = [[1],[2],[3],[4]]
b = copy.copy(a)
assert b == a
b = copy.deepcopy(a)
assert b == a

a = [1,2,3,4]
b = a
b[0] = 3
assert b == a

a = [1,2,3,4]
b = a
b = copy
