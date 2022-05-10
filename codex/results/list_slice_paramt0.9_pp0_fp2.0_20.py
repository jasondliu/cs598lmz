import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
import gc;gc.colle0()
if lst[0] is not '':raise ValueError,'Failed str reference count test'
del a
lst[:]=[]
def callback(x):lst.append(True)
a=Object()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
import gc;gc.colle0()
if len(lst)!=1:raise ValueError,'Failed Object reference count test'
del keepali0e
class Foo(object):
	def __init__(self,x):self.__x=x
	def meth1(self):pass
f=Foo(1)
f.meth1()
class OldStyle:pass
o=OldStyle()
f.meth1(o)
del f,OldStyle,o
class OldStyle:
	def meth1(self):
		if not hasattr(self,'__x'):return -1
		else:return self.__x
	def meth2(self
