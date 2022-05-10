import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(a)
a.a=a
a.b=weakref.ref(a,callback)
print(lst)
assert len(lst)==1
del a
lst[0]+=str()
print(lst)
