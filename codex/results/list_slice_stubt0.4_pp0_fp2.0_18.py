import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.a=weakref.ref(a,callback)
print(lst)
del a
print(lst)
del lst[0]
print(lst)
del keepalive[0]
print(lst)

#['']
#['']
#[]
#[]
#[Finished in 0.2s]
