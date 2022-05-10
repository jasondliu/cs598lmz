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

# 弱引用的另一个用途是缓存，当缓存的数据量超过某个阈值时，就可以删除最早没有被使用的项。
# 下面的例子演示了如何利用 WeakValueDictionary 来实现一个简单的缓存：
import weakref
class Cache(object):
    def __init__(self,size):
        self.size=size
        self.cache={}
        self.access=[]
    def __getitem__(self,key):
        try:
            value=self.cache[key]()
        except KeyError:
            raise KeyError(key+'not found')
       
