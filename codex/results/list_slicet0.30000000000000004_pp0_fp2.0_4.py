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

# 执行结果：
# [<weakref at 0x0000027C6E9C9D38; to 'A' at 0x0000027C6E9C9B70>, ['']]
# 分析：
# 循环引用导致的内存泄漏，导致程序无法正常退出。
# 使用weakref模块，可以解决这个问题。
# 使用weakref模块中的弱引用，可以解决循环引用的问题。
# 弱引用，不会增加对象的引用计数，
