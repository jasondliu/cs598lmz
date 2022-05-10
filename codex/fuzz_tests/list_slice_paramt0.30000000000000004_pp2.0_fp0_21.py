import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#结果是：['a']
#因为a.c=a，a和a.c引用了同一个对象，所以a.c也被引用了，所以a不会被回收

#判断一个对象是否被引用
import gc
a=A()
b=A()
a.b=b
b.a=a
print(gc.get_referents(a))
print(gc.get_referents(b))

#结果是：
#[<__main__.A object at 0x0000024A4C7A4128>, <__main__.A object at 0x0000024A4C7A4160>]
#[<__main__.A object at 0x0000024A
