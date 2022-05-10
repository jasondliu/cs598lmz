import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
gc.collect()
from gc import collect
collect()
for o in gc.get_objects():
    if isinstance(o,str) and o is not lst[0]:
        print o,''.center(60,'*')
str2obj.clear()
str2obj[lst[0]]=lst
for o in gc.get_objects():
    if isinstance(o,str) and o is not lst[0]:
        print o,'*'.center(60,'*')
lst.append('')
for o in gc.get_objects():
    if isinstance(o,str) and o is not lst[0]:
        print o,'*'.center(60,'*')
lst[0]='a'
for o in gc.get_objects():
    if isinstance(o,str) and o is not lst[0]:
        print o,'*'.center(60,'*')

