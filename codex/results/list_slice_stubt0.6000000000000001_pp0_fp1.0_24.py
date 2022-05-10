import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(a.c)
lst.append(weakref.ref(a,callback))
del a
print lst
keepalive.append(lst)
del lst
keepalive.append(str())
print keepalive
del keepalive
print keepalive
#print a
gc.collect()
print keepalive
#print a
#print lst

#print a
