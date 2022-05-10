import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst

y = A()
y.c = y
lst = [str()]
keepalive=[]
keepalive.append(weakref.ref(y, callback))
lst

# 弱引用不会阻止对象销毁,类似垃圾回收机制
# 这种弱引用性质可以利用它来实现缓存功能
# 如果缓存的对象数量超过一定数量,那么它可以使用弱引用来避免内存占用

class cache():
    def __init__(self,size):
        self.max_size=size
        self.cache={}
        self.order=[]
       
