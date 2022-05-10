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

#这个例子中，对象a是循环引用的，因此不会被回收，但是a.c是弱引用，因此仍然会被回收，这样就会调用回调函数，删除lst中的元素，因此lst中只剩下一个空字符串。

# 弱引用的另一个用途是在缓存中使用。例如，下面的代码实现了一个简单的缓存，它只能缓
