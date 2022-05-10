import weakref
# Test weakref.ref() 

import weakref

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
# <weakref at 0x10f8b6f28; to 'C' at 0x10f8b6e10>
print(o)
# <__main__.C object at 0x10f8b6e10>
print(r() is o)
# True
del o
# 当对象被删除后，引用指向None
print(r())
# None

############################################################################################
"""
weakref模块的第二个方法是weakref.proxy()。这个函数创建一个对象的弱引用，但返回的不是引用对象，而是它的代理对象。
当原
