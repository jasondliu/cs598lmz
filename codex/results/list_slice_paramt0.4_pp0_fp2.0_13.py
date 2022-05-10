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
del a.c
print lst

# 用弱引用来记录缓存数据,当内存不足时,可以自动回收
import weakref
class CachedSpamManager(object):
    def __init__(self):
        self._cache=weakref.WeakValueDictionary()
    def get_spam(self,name):
        if name not in self._cache:
            s=Spam(name)
            self._cache[name]=s
        else:
            s=self._cache[name]
        return s

# 对于需要持久化的对象,可以使用代理类来代理,这样可以把持久化的数
