import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.c=weakref.ref(a,callback)
print(lst)
del a
print(lst)
del keepalive
print(lst)

#['']
#['']
#[]
