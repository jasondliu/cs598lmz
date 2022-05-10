import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst.append(weakref.ref(lst,callback))
del lst
print(keepalive)

# 弱引用的一个重要用途是实现缓存。
# 例如，你可以使用一个字典并将弱引用放入其中来构造一个简单的缓存。
# 下面是一个例子，它使用一个类来演示这种方式：
import weakref
class Cache(object):
    def __init__(self,size):
        self.size=size
        self.cache={}
        self.access=[]
    def get(self,key):
        try:
            value=self.cache[key]()

