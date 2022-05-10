import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect to make sure the weakref can be called
g=1
r=weakref.ref(g)
del g
gc.collect()
print(r())

class Test1:
    def f(self):
        return str(self)

gc.collect()

t=Test1()
d=[t, t.f, t.f()]
t.f()
d.append(t.f)
del t

gc.collect()
print(d)

# test if __del__ is properly called in gc
class Test2:
    def __del__(self):
        print(self, 'deleted')

gc.collect()

t2=Test2()
print(t2)
del t2
gc.collect()

class Test3:
    pass

gc.collect()

t3=Test3()
t3.a=t3
del t3
gc.collect()

import sys
# test gc cyclic with __del__ method
class Test4:
    def __del__(self):
        print('deleted')
