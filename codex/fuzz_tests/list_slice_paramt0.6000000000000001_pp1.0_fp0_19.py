import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
del a
print(lst)

"""
"""
def f():
	pass
f()
print(f.__name__)

def f2(name):
	return name
print(f2("zhangsan"))


def f3(name):
	def ff(name):
		return name
	return ff(name)
print(f3("zhangsan"))

def f4(name):
	return name
print(f4("zhangsan"))

def f5(name):
	def ff(name):
		return name
	return ff(name)
print(f5("zhangsan"))

def f6(name):
	def ff(name):
		return name
	return ff(name)
print(f6("zhangsan"))

def f7(name):
	def ff(name):
		return name
	return ff(name)
print(f7("zhangsan"))

def f8(name):
	def ff(name):
		return name
	return ff(name
