import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=[1,2,[3,4,a]]
a.a=a.b[2]
keepali0e.append(a.b)
keepali0e.append(a.a)
keepali0e[0].append(weakref.ref(lst,callback))
gc.collect()
print lst
