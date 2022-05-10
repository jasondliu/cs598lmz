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
lst[0]=a
lst[0]='abc'
lst[0]=weakref.ref(lst,callback)
print(lst)
del lst[0]
print(lst)
