import weakref
# Test weakref.ref

##import gc

class A:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return "A(%s)" % self.name


a = A("a")
##a = A("a")
b = weakref.ref(a)
print(b)

print(b())
##print(b())

del a

gc.collect()
print(b())

print(b() is None)

##import gc
##class A:
##	def __init__(self, name):
##		self.name = name
##
##	def __repr__(self):
##		return "A(%s)" % self.name
##
##a = A("a")
##print(a)
##
##b = weakref.ref(a)
##print(b)
##
##print(b())
##
##del a
##
##gc.collect()
##print(b())
##
##print(b() is None)
