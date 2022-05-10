from types import FunctionType
a = (x for x in [1])
print type(a)

def test():
	pass

t = test
print type(t)
print type(test)
print isinstance(t, FunctionType)

def test2(x):
	print x
print test2(5)
print type(test2)

def test3(x):
	return x
print test3(5)
print type(test3)

def test4(x):
	yield x
print test4(5)
print type(test4)

print type(test4(5))

print type(test4)
print type(test4(5))

class A(object):
	pass

a = A()
print type(a)
