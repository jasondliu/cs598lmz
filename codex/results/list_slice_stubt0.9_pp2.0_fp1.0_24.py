import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
weakref.ref(a,callback)

def f():
	class B(object):pass
	o=B()
	def callback():pass
	keepalive=[B]

def g():
	class C(object):pass
	o=C()
	keepalive=[C]

def h():
	class D(object):pass
	o=D()
	def callback():pass
	keepalive=[D]
