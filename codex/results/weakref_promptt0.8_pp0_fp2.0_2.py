import weakref
# Test weakref.ref() as it can give obscure errors
class MyClass(object):
    pass
a = MyClass()
ah = weakref.ref(a)
# This gives obscure error if ah.__class__ does not exist
ah.__class__
# Test weakref.KeyedRef()
class MyClass(object):
    pass
a = MyClass()
class MyClass2(object):
    pass
ah = weakref.KeyedRef(a, MyClass2)
ah

 
# Test weakref.getweakrefs()
class MyClass(object):
    pass
a = MyClass()
ah = weakref.ref(a)
l = weakref.getweakrefs(a)
l[0]()

 
# Test weakref.getweakrefcount()
class MyClass(object):
    pass
a = MyClass()
ah = weakref.ref(a)
weakref.getweakrefcount(a)

 
# Test weakref.WeakValueDictionary()
class MyClass(object):
    pass
d = weakref.WeakValueDictionary()
a = My
