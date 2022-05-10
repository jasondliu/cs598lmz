import types
# Test types.FunctionType
try:
	types.FunctionType
except AttributeError:
	print('SKIP')
	raise SystemExit

def test1():
	pass

x = test1
print(type(test1), type(x), x.__name__, x.__code__.co_name)
x = lambda: 0
print(type(x))

# Custom function type.
class MyFunc(types.FunctionType):
	a = 10

def foo(): print(1)
foo.foo = 'bar'
f = MyFunc(foo.__code__, {}, 'foo', (1,), (1,), None, None, True, foo.__closure__)
print(type(f))
print(f.a)
print(f.foo)
f()
