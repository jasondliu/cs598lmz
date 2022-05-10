import weakref
# Test weakref.ref()
import operator, sys
class MyObject(object):
    def myMethod(self):
        pass
ob = MyObject()
r = weakref.ref(ob)
print(r.__repr__())
# 'e.__repr__()' differs from 'repr(e)' in that it describes the
# type of instance e as well as its contents.
# Below we create two instances of the class from above.
# The function returns a repr. string, so each repr. string
# will be printed on a separate line on stdout
def repr_func(inst):
    return repr(inst)
r1 = weakref.ref(ob, repr_func)
r2 = weakref.ref(ob)
print(r1)
print(r2)
r1()
r2()
r1 = weakref.ref(42, lambda _: 'fortytwo')
r2 = weakref.ref(42)
print(r1)
print(r2)
# Test weakref.proxy()
# Create a proxy object p
ob = MyObject()
p = weakref
