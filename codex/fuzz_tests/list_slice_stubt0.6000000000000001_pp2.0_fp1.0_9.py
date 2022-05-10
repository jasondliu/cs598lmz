import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=lst
keepalive.append(a)
del a
lst[0]='a'
keepalive.append(lst)
del lst
keepalive[0].c=None
keepalive[0].d=None
del keepalive[0]
gc.collect()
print('ok')
