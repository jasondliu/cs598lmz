import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print len(keepali0e)
'''

import gc,gc_test
gc.disable()
a=gc_test.A()
b=gc_test.A()
a.a=b
a.b=b
b.a=b
b.b=b
a.c=a
b.c=b
lst=[a,b]
del a,b

while lst:lst.append(lst[:])
