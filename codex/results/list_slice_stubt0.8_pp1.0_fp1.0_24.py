import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
del a
for i in range(100):lst.append(A())
for i in range(100):lst[i].c=lst[i+1]
del lst[-1].c
del lst[0]
gc.collect()
lst[0]=lst[0].c
a=lst[0]
lst=[]
try:a.c.c
except AttributeError:pass
else:raise AssertionError
try:a[0]
except TypeError:pass
else:raise AssertionError
del a;gc.collect()
assert weakref.getweakrefcount(A)==0
