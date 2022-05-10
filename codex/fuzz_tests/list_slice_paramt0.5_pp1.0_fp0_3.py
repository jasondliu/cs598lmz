import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]

#输出：
# <weakref at 0x0000029F3E1C3F08; to 'A' at 0x0000029F3E1C3F48>
# <weakref at 0x0000029F3E1C3F08; to 'A' at 0x0000029F3E1C3F48>
# <weakref at 0x0000029F3E1C3F08; to 'A' at 0x0000029F3E1C3F48>
# <weakref at 0x0000029F3E1C3F08; to 'A' at 0x0000029F3E1C3F48>
# <weakref at 0x0000029F3E1C3F08; to 'A' at 0x0000029F3E1C3F48>
# <weakref at 0x0000029F3E1C3F08; to 'A' at 0x0000029F3E1C3F48>
# <weakref at 0x00000
