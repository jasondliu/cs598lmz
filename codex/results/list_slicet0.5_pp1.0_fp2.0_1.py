import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(lst)

#如果你想构造一个弱引用的字典，并且希望它的值也是弱引用的，那么你需要自己去实现。
# 下面是一个例子：
import weakref
class StrKeyDict0(dict):
    def __missing__(self,key):
        if isinstance(key,str):
            raise KeyError(key)
        return self[str(key)]
    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return default
    def __contains__(self,key):
        return key in self.keys() or str(key) in self.keys()
d=StrKeyDict0([('2','two'),('4','four')])
print(d['2'
