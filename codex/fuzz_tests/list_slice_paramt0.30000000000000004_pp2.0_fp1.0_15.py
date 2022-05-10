import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst
print keepali0e

#['']
#[<weakref at 0x00000000022E5C18; dead>]

# 注意：
# 弱引用的回调函数不会在删除对象时立即调用。
# 回调函数会在下一次垃圾回收时调用。
# 可以使用 gc.collect() 来强制调用垃圾回收。
# 如果一个对象有多个弱引用，那么它的回调函数会在所有弱引用被删除后才调
