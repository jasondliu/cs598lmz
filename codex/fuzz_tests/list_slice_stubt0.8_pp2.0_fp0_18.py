import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive.append(a)
del lst[0]
del keepalive[0]
a.b=a
lst[0]=a
del lst[0]
del keepalive[0]

import weakref
class A(object):pass
a=A()
weakref.ref(a,callback)
del a

import weakref
def callback(self,x):del self.data[0]
class A(object):
	class Data:
		def __init__(self,data,callback):
			self.data=data
			self.callback=callback
		def __del__(self):
			self.callback(self)
	def __init__(self):
		self.data=[]
	def add(self,x):
		self.data.append(A.Data(x,self.callback))
	def callback(self,x):
		del self.data[0]

import weakref
def callback(self,x):del self.data[0
