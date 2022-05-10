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

# 利用weakref模块实现一个简单的缓存
import time
import weakref
class Cache:
    def __init__(self,size=32):
        self.size=size
        self.mapping={}
    def __getitem__(self,key):
        now=time.time()
        try:
            value,last_update=self.mapping[key]
            if self.has_expired(last_update):
                raise KeyError
        except KeyError:
            value=self.get(key)
            self.mapping[key]=[value,now]
        return value
    def __contains__(self,key):
        try:
            value,last_update=self.mapping[key]
            if self.has_expired(last_update):
                raise KeyError
        except KeyError:
            return False
        return True
    def get(self
