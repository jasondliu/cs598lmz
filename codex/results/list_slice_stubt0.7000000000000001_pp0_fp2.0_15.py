import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.d=a
keepalive.append(a)
a.e=weakref.ref(a,callback)
print(lst)
del a
print(lst)
del keepalive[0]
print(lst)
print(lst)
 
##['']
##['']
##[]
##[]
