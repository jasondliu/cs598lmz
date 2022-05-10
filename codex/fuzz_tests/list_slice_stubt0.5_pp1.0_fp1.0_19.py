import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
w=weakref.ref(a,callback)
print(lst)
print(w)
del a
print(lst)
print(w)
del lst[1]
print(lst)
print(w)
