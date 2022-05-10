import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.s=str()
lst[0]=a
lst[0].ar=lst
lst[0].ref=weakref.ref(lst,callback)
lst[0].ref()
def a():keepalive.append(a)
print(hash(a))
print(hash('aaa'))
