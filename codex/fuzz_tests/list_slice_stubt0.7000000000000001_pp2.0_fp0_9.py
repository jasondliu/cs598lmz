import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a#make a reference cycle
lst[0]=a#make a weak reference to it
weakref.ref(a,callback)
print(keepali0e[0])

#运行结果
#<weakref at 0x00D3C3E8; to 'A' at 0x00D3C3D0>
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


## 弱引用
class A(object):pass
a=A()
w=weakref.ref(a)
print(w)
a=None
print(w)

#运行结果
#<weakref at 0x00D3C330; to 'A' at 0x00D3C2E8>
#<weakref at 0x00D3C330; dead>
#
#
#
#
