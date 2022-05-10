import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e

#缺陷：
#   1.python中的gc模块自己运行时，不触发回调
#   2.finalize不会立即生效，可能要等到gc模块真正奖励对象回收时才会执行
#
#优点：
#   1.可以在计算时释放
#   2.可以自定义监控触发条件

import weakref
class A(object):pass
lst=[]
a1=A()
a2=A()
lst.append(weakref.finalize(a1,lambda:print('a1被回收')))
l
