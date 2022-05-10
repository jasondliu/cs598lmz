import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

'''

class A(object):
	def __init__(self,name):
		self.name=name
	def __del__(self):
		print 'del %s'%self.name

class B(object):
	def __init__(self,name):
		self.name=name
	def __del__(self):
		print 'del %s'%self.name

def callback(x):
	print 'callback'
	del lst[0]

keepalive=[]
lst=[str()]
a=A('a')
b=B('b')
a.b=b
b.a=a
keepalive.append(weakref.ref(a,callback))
del a
del b
print lst

'''
