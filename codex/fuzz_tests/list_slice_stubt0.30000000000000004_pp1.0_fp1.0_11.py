import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepalive.append(a)
w=weakref.ref(a,callback)
print(w)
del a
print(w)
print(lst)
print(keepalive)
del keepalive
print(lst)
print(w)
print(w())
