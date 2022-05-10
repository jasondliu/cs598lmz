import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=weakref.ref(a,callback)
del a
lst #[<weakref at 0x7f7e78cf28e8; dead>]

lst #[<weakref at 0x7f7e78cf28e8; to 'A' at 0x7f7e78cf28d0>]
lst[0]().c is lst[0]() #True
del lst[0]().c #解除弱引用
lst #[<weakref at 0x7f7e78cf28e8; dead>]

import weakref
import gc
#如果要成功使用weakref模块，则必须要引用，而不是直接使用对象。
#安全地使用weakref.ref创建弱引用
class ExpensiveObject(object):
