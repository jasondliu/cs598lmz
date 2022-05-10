import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(len(keepali0e),lst)
del a
print('now',len(keepali0e),lst)
lst[0]='abc'
print('now',len(keepali0e),lst)
