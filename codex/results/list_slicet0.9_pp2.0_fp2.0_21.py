import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])#用于触发callback
for l in keepali0e:print l
#输出:<weakref at 0x01D03F08; to 'A' at 0x01D04030>
#


def qk(obj,callback=None):
    if callback is None:
        def callback(r):obj.__callbacks__.remove(r)
    return weakref.ref(obj,callback)
def keep():#添加了keep方法进行容器操作，维护容器的有效引用
    if not hasattr(keep,'cache'):keep.cache=[]
    container=keep.cache
    def _(obj):#非标准的用法
        if hasattr(obj,'__callbacks__'):
            for r in obj.__callbacks__.copy():
                refer=r()
                if refer is None:
                    obj.__callbacks__.remove(r)
