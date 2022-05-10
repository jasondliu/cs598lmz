import types
types.ClassType

# using 'classmethod' decorator, the first argument of instance methods is always a 'class'
# but without 'classmethod' decorator, the first argument of a instance methods is always an object: self
class A:
	def foo(x):
		print "executing foo(%s)"%(x)
	def class_foo(cls, x):
		print "executing class_foo(%s, %s)" % (cls, x)
	class_foo = classmethod(class_foo)
a = A()

## execute a.foo(1) failed --> TypeError: unbound method foo() must be called with A instance as first arguement (got int instance instead)
a.foo(1)
## execute A.foo(1)
A.foo(1)
## execute a.class_foo(1)
a.class_foo(1)
## execute A.class_foo(1)
A.class_foo(1)

## a.foo(), execute foo() method, the instance variable will be 'self' by default, so we
