import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
#print lst
#print a
#print keepalive
lst[0]=a
#print a
#print lst
del a
#print lst
#print keepalive
weakref.ref(lst[0],callback)
#print lst
#print keepalive
del lst
#print keepalive
