from types import FunctionType
a = (x for x in [1])
a[0]

b = [1,2]
c = ["a", "b"]
d = [True, False]
e = [a, b, c, d]
e

def f(x):
	return x + 1

f1 = [f, a]

f2 = map(f, [1,2,3,4])


class A:
	def __init__(self, x):
		self.x = x
		
	def foo(self, amt):
		self.x += amt


class B(A):
	def bar(self, amt):
		self.x += amt


a = A(1)
b = B(2)

print "b.foo(1):"
b.foo(1)
print b.x

print "a.bar(1):"
a.foo(1)
print a.x

print "b.bar(1):"
b.bar(1)
print b.x

print "b.__class__:"
print b
