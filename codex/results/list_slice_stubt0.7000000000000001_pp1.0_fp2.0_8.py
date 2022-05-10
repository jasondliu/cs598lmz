import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
lst.append(a)
del lst
lst=[str(),str()]
a.c=a.b=a
keepali0e.append(a)
lst.append(a)
lst[0]=lst[1]
lst.pop(1)
lst.pop()
weakref.finalize(a,callback,lst)
print(lst)
a=lst[0]
del a
del lst
del a
print(lst)
del keepali0e
