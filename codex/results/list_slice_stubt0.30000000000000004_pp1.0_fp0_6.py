import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
keepali0e.append(callback)
keepali0e.append(lst[0])
del a,lst
gc.collect()
print(keepali0e)

# 测试结果：
# [<__main__.A object at 0x000002A6E5D6D828>, <__main__.A object at 0x000002A6E5D6D828>, [''], <function callback at 0x000002A6E5D6D950>, '']
# 可以看到，lst[0]是''，说明lst[0]已经被回收了，但是callback函数依然存在，
# 这说明，当lst[0]被
