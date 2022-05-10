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
print(lst)
#['<weakref at 0x0000000003D7E7C8; to 'A' at 0x0000000003D7E908>']

#第二种情况：
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
print(lst)
#['<weakref at 0x0000000003D7E7C8; to 'A' at 0x0000000003D7E908>']

#第三种情况：
import weakref
class A(object):pass
