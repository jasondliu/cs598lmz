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
print keepali0e

#输出：
#[<weakref at 0x0000000002A8D948; to 'A' at 0x0000000002A8D908>, []]
#第一个元素是一个弱引用，第二个元素是一个空列表，说明弱引用被回调函数删除了。

#弱引用的另一个用途是实现缓存。
#比如我们要实现一个缓存，缓存最多1000个对象，当缓存满了，就删除最早没有被访问的对
