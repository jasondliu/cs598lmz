import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
del lst,a
for i in range(2):
    lst=[str()]
    a=A()
    lst.append(a)
    keepalive.append(lst)
    a.b=str()
    a.c=a
    a.b=weakref.ref(a,callback)
    del a,lst
    print('lives:',list(gc.get_objects()))
    print('garbage:',gc.garbage)
    print()
