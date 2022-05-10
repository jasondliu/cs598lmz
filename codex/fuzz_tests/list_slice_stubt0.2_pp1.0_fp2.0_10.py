import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)

# 弱引用的另一个用途是实现缓存，比如，你可以用它来缓存文件的内容：
import weakref
class Cache(object):
    def __init__(self,size):
        self.size=size
        self._cache={}
        self._cache_keys=[]
    def __getitem__(self,key):
        try:
            value=self._cache[key]()
            if value is None:
                raise KeyError(key)
            return value
        except KeyError:
            value=self.get(key)
            self._cache[key]=weakref.ref(value)
            self._cache_keys.append(key)
            if len(self._cache_keys)>self.size:
               
