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

# 打印结果：
# [<weakref at 0x000002A7D2F0A848; to 'A' at 0x000002A7D2F0A898>, []]
# 可以看到，在删除a之后，lst中的元素被删除了。
# 这是因为，当a被删除后，a.c也被删除了，而a.c指向a，所以a也被删除了。
# 因此，a.c指向a的引用计数变为0，回调函数被调用，删
