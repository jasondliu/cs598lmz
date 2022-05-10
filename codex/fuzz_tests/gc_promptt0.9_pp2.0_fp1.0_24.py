import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect(), with and without x_refs argument.

class A:

    def __init__(self):
        self.__class__.x_ctr += 1

    def __del__(self):
        self.__class__.x_ctr -= 1

    def f1(self):
        #print "A.f1:", self.__class__.x_ctr
        self.__class__.x_ctr += 1

    def f2(self):
        #print "A.f2:", self.__class__.x_ctr
        self.__class__.x_ctr += 1

def f():
    A.x_ctr = 0
    a = A()
    l = []

    # create a cycle and put it on weakref.ref(a) referents list
    a.x = a
    r = weakref.ref(a)
    l.append(r)

    # make some other garbage
    for i in range(15):
        l.append({})
        copyreg.dispatch_table.clear()
        l = []

   
