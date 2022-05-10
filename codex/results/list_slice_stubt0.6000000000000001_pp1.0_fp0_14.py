import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
keepalive.append(a)
keepalive.append(b)
a.b=weakref.ref(b,callback)
b.a=weakref.ref(a,callback)
del a
del b
del keepalive
assert not lst
lst=[str()]
a=A()
b=A()
a.b=weakref.ref(b,callback)
b.a=weakref.ref(a,callback)
del a
del b
del keepalive
assert not lst
print "OK"

class B(object):
	def __init__(self,x):
		self.x=x
	def __eq__(self,other):
		return self.x==other.x
class C(object):
	def __init__(self,x):
		self.x=x
	def __eq__(self,other):
		return self.x==other.x
	def __hash__(self):
		return self.x
class D(object
