import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])#print keepali0e[-1],len(lst)
#print keepali0e
#print keepali0e
for i in keepali0e:
	print i

'''
import gc
gc.disable()
l=[str()]
while l:l.append(l[:])#print l[-1],len(l)
'''
'''
def dealloc(x):print "dealloc",x
class A(object):
	def __init__(self,name):
		self.name=name
	def __del__(self):
		print "del",self.name
	def __repr__(self):
		return self.name
a=A("a")
b=A("b")
a.c=b
b.c=a
b=None
del a
import gc
gc.disable()
print gc.collect()

import weakref

class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=
