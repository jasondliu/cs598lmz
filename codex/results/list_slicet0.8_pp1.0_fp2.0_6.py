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
#运行后结果为[[], [str(), str()], [str(), str()], [str()], [str()], [str()]]。
#如果把第4行的第二个参数callback改为None，则打印结果为[[], [str(), str()], [str(), str()]]。
#
'''
——1.11.2 弱引用的缺陷
　　弱引用很明显的缺陷就是，不能保留对象的实例化状态。如果被弱引用的对象被销毁，那么所有的弱引用都将失效
