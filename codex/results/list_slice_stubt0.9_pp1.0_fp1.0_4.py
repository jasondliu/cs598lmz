import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.c.c=a
lst[0]=a
wr=weakref.ref(a,callback)
lst[0]=None
print keepalive
del a
print keepalive
print a

#类，继承，多重继承
class A(object):
	def __init__(self):
		self.a=1
class B(object):
	def __init__(self):
		self.b=1
class C(A,B):
	def __init__(self):
		super(C,self).__init__();
		self.c=1
C().c	
class A(object):
	def __init__(self):
		self.a=1
class B(object):
	def __init__(self):
		self.a=2
class C(A,B):
	def __init__(self):
		self.c=1
C().a

setattr(C,"a",10)
C().a
