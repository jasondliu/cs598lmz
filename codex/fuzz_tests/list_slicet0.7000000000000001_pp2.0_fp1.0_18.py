import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
del keepali0e

class NastyList(list):
	def __del__(self):del lst[0]
lst=[str()]
keepalive=[]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
nasty=NastyList()
keepalive.append(nasty)
nasty.append(a)
del a
del nasty
del keepalive[:]
while lst:keepalive.append(lst[:])
del keepalive
