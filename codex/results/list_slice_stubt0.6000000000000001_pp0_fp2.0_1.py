import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
lst.append(weakref.ref(a,callback))
a=None
import gc
for i in range(2):
    gc.collect()
    print(len(lst))
del lst
del keepali0e
gc.collect()
print(gc.garbage)

#Output:
#2
#2
#['']
