import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
del keepalive
lst.append(A())

class Base(object):pass
class Sub(Base):pass
class X(Base):pass
X()
b=Base()
del b
b=Base()
Base=1
Base
Base.__class__
'.'.join(X().__class__.__module__.__class__.__mro__[-3].__name__.__class__.__mro__[0].__subclasses__()[40].__name__.__mro__[1].__subclasses__()[59].__name__.__mro__[1].__subclasses__()[49].__name__.__mro__[0].__subclasses__()[79].__name__.__mro__[-2].__subclasses__()[87].__name__.__mro__[0].__subclasses__()[88].__name__.__mro__[0].__subclasses__()[11].__name__.__mro__[0].
