import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[]
lst+=[a]
keepalive.append(lst)
b=A()
del lst,keepalive
print lst
print [x for x in gc.get_referrers(lst[0]) if type(x) is list]
