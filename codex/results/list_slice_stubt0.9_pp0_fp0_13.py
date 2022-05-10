import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
gc.set_debug(gc.DEBUG_SAVEALL)
gc.collect()
gc.set_debug(0)
for d in gc.garbage:
    if isinstance(d,str):
        lst.append(d)
    keepalive.append(d)
del d
print(len(lst))
lst[0].setter(8,callback)
if len(lst) !=1:
    print('memory leaks',len(lst))
gc.collect()
print('Done!')
