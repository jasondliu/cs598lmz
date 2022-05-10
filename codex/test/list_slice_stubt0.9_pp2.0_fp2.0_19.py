import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.z=lst
b=A()
lst.append(b)
b.a=a
lst[0]="""
def callback(x):
	x()
"""
callback(lambda :keepalive.append(lst))
del a
del b
