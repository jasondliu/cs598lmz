import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=a
a.c=lst
keepalive=lst
w=weakref.ref(lst,callback)
print(lst)
