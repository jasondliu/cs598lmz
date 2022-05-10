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
import gc
gc.collect()
lst

#output:
#['<cell at 0x7f1fcc5e2d20: str object at 0x7f1fcc532a80>']

#2.4
#python 2.4 以下版本中可能会发生死锁（deadlock）：
1.手动调用gc模块，且正在收集循环引用的类的实例的弱应用时，使用了threading模块的线程。
2.程序同时运行新的线程，并且gc模块正在收集循环引用的类的实例的弱引
