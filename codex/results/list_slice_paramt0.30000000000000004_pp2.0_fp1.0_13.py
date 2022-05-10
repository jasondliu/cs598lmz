import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#这个例子中，a.c=a，a引用了自己，这样a就不会被回收，但是当a被回收时，a.c也会被回收，因此a.c被回收时，callback会被调用，删除lst中的元素，所以lst中的元素会被删除

#利用弱引用实现缓存
import weakref
class Cache:
    def __init__(self,size=32):
        self.size=size
        self.cache={}
        self.access=[]
    def __getitem__
