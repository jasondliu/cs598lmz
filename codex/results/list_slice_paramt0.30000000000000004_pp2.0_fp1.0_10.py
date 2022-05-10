import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
gc.collect()
print(lst)

# 弱引用的另一个用途是为了实现一个缓存，当缓存的对象不再被使用时，它会被自动清除。
# 例如，下面是一个简单的缓存实现：
import weakref
class Cache(object):
    def __init__(self,size):
        self.size=size
        self.cache=weakref.WeakValueDictionary()
    def get(self,key):
        try:
            return self.cache[key]
        except KeyError:
            value=self.fetch(key)
            self.cache[key]=value
           
