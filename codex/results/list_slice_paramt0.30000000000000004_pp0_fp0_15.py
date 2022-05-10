import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print lst
del a
print lst

# 这个例子中，对象a的弱引用被存储在keepalive中，当a被删除时，它的弱引用被调用，但是因为a.c指向a本身，所以a不会被回收，直到keepalive中的引用被删除。
# 当keepalive中的引用被删除时，回调函数被调用，它删除了lst中的第一个元素。这样，a的引用计数就变
