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
[method()for method in(
[setattr, hasattr, getattr, object.__repr__, object.__str__,
object.__unicode__,object.__hash__,object.__setattr__,
object.__delattr__,object.__sizeof__,object.__nonzero__,
object.__cmp__,object.__getattribute__,object.__getnewargs__,
object.__class__,object.__reduce__,object.__reduce_ex__,
object.__dict__,object.__dir__,object.__format__,object.__getstate__,
object.__setstate__,object.__getnewargs_ex__,object.__getattribute__,
object.__gt__,object.__ge__,object.__lt__,object.__le__,object.__eq__,
object.__ne__,object.__del__,object.__init__,object.__new__])for x in lst]
</code>
But, the only thing I'm actually looking for is the source code of the <
