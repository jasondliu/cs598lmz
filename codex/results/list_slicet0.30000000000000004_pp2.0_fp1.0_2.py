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

# 测试：
# 在Python3.6.3中，输出：
# [<weakref at 0x0000020D5F9C0C48; dead>, ['']]
# 在Python2.7.13中，输出：
# [<weakref at 0x00000000020D5F9C0C48; dead>, ['']]
# 在Python3.6.3中，输出：
# [<weakref at 0x0000020D5F9C0C48; dead>, ['']]
# 在Python2.7.13中，输出：
# [<weakref at 0x00000000020D5F9C0C48; dead>, ['']]
# 在Python3.6.3中，输出：
# [<weakref at 0x0000020D5F9C0C48
