import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
lst[0]=1
lst.append(2)
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(b,callback))
keepalive.append(lst)
print len(lst)
print a
print b
print lst
del lst
print a
print b
