import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with nested weakref attrs from class and instance
# 1.5) Create a class, with a __del__.
class C:
    def __del__(self):
        print "del"
    def __delattr__(self,attrname):
        object.__delattr__(self,attrname)
        print "attr del",attrname
o=C()
o.x=12
# Attr o.y will be deleted, which will collect o.x and o
o.y=weakref.ref(o,(lambda:print "callback"))
# 2) Modify attr so __del__ isn't called when collecting the implicitly-deleteable attr.
# 2.1) Profilable test
del o
o=C()
# Register a deleter for id(o), then delete o, then create a weakref to object id, requring a collect.
weakref.weakref(o,(lambda : print "callback"))
del o
gc.collect()
# 2.2) Non-profilable test
del o
o=C()
# Register a deleter for id
