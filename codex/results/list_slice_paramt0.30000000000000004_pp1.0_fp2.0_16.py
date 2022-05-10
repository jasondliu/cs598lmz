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

#结果为：['\x00']
#这个结果表明，即使a.c=a，也不会导致循环引用，因为a.c是一个弱引用。

#弱引用的另一个用途是缓存。
#缓存是一种常见的设计模式，它的目的是避免重复计算或者重复加载数据。
#下面的例子是一个简单的缓存，它可以记住上一次计算的结
