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
