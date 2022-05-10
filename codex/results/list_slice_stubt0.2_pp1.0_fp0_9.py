import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
import gc
gc.collect()
print lst
print keepalive

#[str(), <weakref at 0x7f6d8c0b0d80; to 'A' at 0x7f6d8c0b0d10>]
#[<__main__.A object at 0x7f6d8c0b0d50>]

#这里的keepalive是一个列表，列表中的元素是一个类的实例，这个实例的属性c是自己，
#这个实例的弱引用被放在了lst列表中，lst列表中的第一个元素是一个字符串
