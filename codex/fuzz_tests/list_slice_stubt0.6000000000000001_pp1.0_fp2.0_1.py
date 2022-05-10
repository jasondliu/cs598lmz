import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=weakref.WeakKeyDictionary(callback)
a.d[a]=None
keepalive.append(a)
del a
del keepalive
gc.collect()
lst[0]

#结果：
#<ref at 0x00000000031D9C08 to str at 0x00000000031D9C40>
#<ref at 0x00000000031D9C08 to str at 0x00000000031D9C40>
#<ref at 0x00000000031D9C08 to str at 0x00000000031D9C40>
#<ref at 0x00000000031D9C08 to str at 0x00000000031D9C40>
#<ref at 0x00000000031D9C08 to str at 0x00000000031D9C40>
#<ref at 0x00000000031D9C08 to str at 0x00000000031D9C40>
#<ref at 0x00000000031D9C08 to str at 0x00000000031D9C40>
#<
