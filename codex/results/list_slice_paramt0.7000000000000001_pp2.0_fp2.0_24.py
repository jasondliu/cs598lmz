import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
print len(keepali0e)
print len(lst)
del a
while keepali0e:
    print len(keepali0e)
    print len(lst)
    print keepali0e[0]()
    del keepali0e[0]
    print len(keepali0e)
    print len(lst)
