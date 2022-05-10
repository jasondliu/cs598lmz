import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
ob=a.c
lst.append(ob)
keepalive=[]
#keepalive.append(ob)
del a
del lst
del ob
#print len(gc.get_referrers(a.c))
#print gc.get_referrers(lst)
a=A()
#strongref=a
a.a=a.b=a.c=a
#strongref2=a.a
