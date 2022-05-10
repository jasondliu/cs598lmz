import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
lst.append(a)
del a
print lst
print keepalive
print len(keepalive)

#结果：
#['', <__main__.A object at 0x000001F0E5F8D5C0>]
#[<__main__.A object at 0x000001F0E5F8D5C0>]
#1
#[Finished in 0.1s]

#结论：
#1、当一个对象的弱引用被删除的时候，回调函数会被调用，并且会传入弱引用的对象
#2、回调函数是在弱引用被删除的
