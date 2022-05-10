from types import FunctionType
list(FunctionType(lambda x: x, globals())(range(1)))

# Test for issue #205
def __repr__(self):
	return 'foo'
class A(object):
	pass
A.__repr__ = __repr__
print(A())

# Test for issue #227 (__repr__ returning string not of type 'str')
print(unicode('foo'))

# Test for issue #219 (KeyError on non-existing keyword argument)
def test_kwargs(x, **kwargs):
	pass
test_kwargs(1)

# Test for issue #215 (KeyError on non-existing keyword argument in __new__)
class A(object):
	def __new__(cls, x, **kwargs):
		pass
A(1)

# Test for issue #213 (SyntaxError on duplicate keyword argument)
def test_kwargs(x, **kwargs):
	pass
test_kwargs(1, x=2)

# Test for issue #215 (SyntaxError on duplicate keyword argument in __new__)
class
