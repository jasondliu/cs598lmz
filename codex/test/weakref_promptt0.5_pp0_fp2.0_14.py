import weakref
# Test weakref.ref(obj)
# Test weakref.ref(obj, callback)
# Test weakref.proxy(obj)
# Test weakref.getweakrefcount(obj)
# Test weakref.getweakrefs(obj)
# Test weakref.finalize(obj, func, *args, **kwargs)
# Test weakref.WeakSet
# Test weakref.WeakKeyDictionary
# Test weakref.WeakValueDictionary

from test.test_support import run_unittest, gc_collect, import_module

#=======================================================================

class Foo(object):
    pass

class Foo2(object):
    pass

class Foo3(object):
    pass

class Foo4(object):
    pass

class Foo5(object):
    pass

class Foo6(object):
    pass

class Foo7(object):
    pass

class Foo8(object):
    pass

class Foo9(object):
    pass

class Foo10(object):
    pass

#=======================================================================

