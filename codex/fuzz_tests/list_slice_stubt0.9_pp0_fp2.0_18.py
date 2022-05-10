import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(callback)
keepali0e.append(lst)

del lst[0],a,callback

gc.collect()
__all__.extend(["N", "M", "lst", "keepali0e"])
__dir__.append("voidstruct"); from voidstruct import *; __all__.append("voidstruct");
import weakref
__all__.extend(["A", "callback", "keepali0e", "lst", "a", "gc", "weakref"])
__all__.extend(["N", "M", "lst", "keepali0e"])
import voidstruct
__imported__["voidstruct"] = voidstruct
__all__.append("voidstruct")
__allexamples__.append(voidstruct)
