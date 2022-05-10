import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=[a,lst,keepali0e,a]
lst[0]=a
keepalive=a
del a
gc.collect()
print(len(lst))

class A(object):
	def __del__(self):
		print('A.__del__')
class B(object):
	def __del__(self):
		print('B.__del__')
		A()
class C(object):
	def __del__(self):
		print('C.__del__')
		B()
lst=[str()]
a=A()
b=B()
c=C()
lst[0]=c
del a,b,c
gc.collect()

class A(object):
	def __del__(self):
		print('A.__del__')
class B(A):
	def __del__(self):
		print('B.__del__')
		A.__del__(self)
class C(B):
	def __del__(self):
