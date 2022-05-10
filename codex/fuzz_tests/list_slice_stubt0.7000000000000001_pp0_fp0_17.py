import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.__dict__[1]='a'
a.__dict__['b']=1.2
a.__dict__[0]=a
a.__dict__[lst]=a
print(lst)
lst[0]=a
lst.append(a)
lst.append(lst)
print(lst)
print(keepali0e)
del a
del lst
print(keepali0e)
print(lst)
keepali0e.append(weakref.ref(lst,callback))
print(keepali0e)
del keepali0e
print(lst)
