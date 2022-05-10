import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
w=weakref.ref(a,callback)
del a,callback
keepalive.append(w)
keepalive.append(w())
keepalive.append(lst)
print(len(del))
