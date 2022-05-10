import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None


import types
from sys import getrefcount
class MyClass(object):
	pass
def func(x):
	return x**2
def count(values,update=False):
	counts={}
	for v in values:
		counts[v]=counts.get(v,0)+1
	if update:
		update(counts)
	return counts
f=func
#print count([1,1,2])
#print isinstance(f,types.FunctionType)
#print issubclass(MyClass,object)
#print isinstance(MyClass,object)
#print isinstance(MyClass(),object)
#print getrefcount(str)
#print getrefcount("")
#print getrefcount("")
#print getrefcount("")
#print getrefcount("")
#print getrefcount("")
#print getrefcount("")


import weakref
import gc
class Node(object):
	def __init__(self,value):
		self.value=value
		
