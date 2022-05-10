import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.lst=lst
a.name='a'
keepalive=[a,lst]
keepali0e.append(weakref.ref(a,callback))
