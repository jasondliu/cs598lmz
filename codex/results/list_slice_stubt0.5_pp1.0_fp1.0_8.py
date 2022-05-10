import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print(lst,keepalive)
del a
print(lst,keepalive)
lst[0]=1
print(lst,keepalive)
