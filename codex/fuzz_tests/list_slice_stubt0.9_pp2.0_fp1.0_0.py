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
gc.collect()
b=lst[0]
lst[0]=str()
#print len(keepalive)
print len(gc.get_referrers(b))
keepalive.append(b)
keepalive2=[]*8
keepalive2.append([])
keepalive2.append([])
lst[0]=b
lst[0]='i'
print gc.get_referrers(lst)
print gc.get_referrers(b)
print gc.get_referrers(a)
print gc.get_referrers(a.
