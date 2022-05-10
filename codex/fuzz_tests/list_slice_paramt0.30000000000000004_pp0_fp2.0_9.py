import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

# 弱引用的另一个用途是实现缓存
import weakref
class Cache(object):
    def __init__(self,size):
        self.size=size
        self.cache={}
        self.access=[]
    def __getitem__(self,key):
        try:
            value=self.cache[key]()
            if value is not None:
                self.access.remove(key)
                self.access.append(key)
                return value
        except KeyError:
            raise KeyError(key+'not found')
        except TypeError:
            del self.cache[key]
            raise KeyError(key+'not found')
    def __setitem__(self,key,value):
        try:
            self.cache[key]=weakref.ref(value)
            self.access.append(key)
            if len(self.access)>self.size:
               
