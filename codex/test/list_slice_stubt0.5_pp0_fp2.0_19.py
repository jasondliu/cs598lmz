import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a.c,callback))
keepali0e.append(lst)
del a
while lst:
    print(lst)
    if not lst:
        lst.append(str())
