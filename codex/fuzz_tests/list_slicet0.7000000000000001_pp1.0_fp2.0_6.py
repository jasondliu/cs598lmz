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

#代码说明：
#1.模拟实现一个循环引用，模拟垃圾回收的情况
#2.通过callback，实现了循环引用的删除
#3.只有当keepali0e里面的引用全部清理了，lst才会被删除
#4.因此，如果想要避免循环引用，需要及时的删除引用，不要再一个循环中去拷贝引用


#关于垃圾
