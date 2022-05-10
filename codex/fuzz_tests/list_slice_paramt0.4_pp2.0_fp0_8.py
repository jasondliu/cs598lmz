import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)
print(keepali0e)
keepali0e[0]()
print(lst)
print(keepali0e)

# 运行结果
# ['abc']
# [<weakref at 0x000001C7E7D8F638; to 'A' at 0x000001C7E7D8F5F8>]
# []
# [<weakref at 0x000001C7E7D8F638; dead>]
