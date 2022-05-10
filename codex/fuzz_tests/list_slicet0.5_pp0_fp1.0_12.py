import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(keepali0e)

#输出
#[<weakref at 0x0000024E8F9D0B88; to 'str' at 0x0000024E8F9D0B40>,
# ['\x00'],
# [<weakref at 0x0000024E8F9D0B88; dead>]]
#
#
