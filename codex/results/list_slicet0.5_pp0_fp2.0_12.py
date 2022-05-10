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

# 二、构造循环引用
# 循环引用可能会导致内存泄漏
import gc
class A(object):
    def __init__(self):
        self.a=self
        self.b=self
class B(object):
    def __init__(self):
        self.a=A()
        self.b=A()
def test():
    a=A()
    b=B()
    del a
    del b
    gc.collect()
    print(gc.garbage)
test()
# 三、多线程
# 当一个线程结束时，它的所有对象都会被垃圾回收器回收
# 而同一个线程中的不同
