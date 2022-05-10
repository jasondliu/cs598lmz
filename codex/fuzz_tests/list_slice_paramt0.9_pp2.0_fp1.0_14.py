import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
assert lst, 'Initial callback did not happen'
del a.c
assert not lst, 'Delayed callback did not happen'
