import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
#keepalive=lst
a.wref=weakref.ref(a,callback)
del a
#lst=[]
print(keepalive)
print(lst)

#lst= [str(), <__main__.A object at 0x0000000002A5B5C0>]

# weakref.ref 只有当需要回调的对象从内存中移除时才会调用
# 比如上面的例子，当del a时，a的引用计数变为0，就会调用回调
# 但是为什么没有del lst[0]呢？
# 因为a.wref是弱引用，它不会增加
