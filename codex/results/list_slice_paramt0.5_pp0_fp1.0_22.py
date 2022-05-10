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
gc.collect()
print(lst)
#['<weakref at 0x000002A7D4C9D4C8; to 'A' at 0x000002A7D4C9D4A8>', '<weakref at 0x000002A7D4C9D4F8; to 'A' at 0x000002A7D4C9D4A8>']


# 删除回调函数
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e[0].callback=None
del a
gc.collect()
print(lst)
#['<weakref at
