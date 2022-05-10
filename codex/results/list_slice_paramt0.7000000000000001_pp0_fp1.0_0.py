import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst.append(weakref.ref(a,callback))
assert lst.__len__()==2
del a
assert lst.__len__()==1
