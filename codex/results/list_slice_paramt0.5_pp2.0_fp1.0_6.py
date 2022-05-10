import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print keepali0e[0]
del a
print keepali0e[0]
print lst[0]
del lst[0]
print keepali0e[0]

#结果为：
#<weakref at 0x00000000024F0C08; to 'A' at 0x00000000024F0B88>
#<weakref at 0x00000000024F0C08; to 'A' at 0x00000000024F0B88>
#
#<weakref at 0x00000000024F0C08; dead>

#结论：
#1.弱引用只会影响引用对象，不会影响引用对象的引用对象
#2.当引用对象被删除时，自动调用回
