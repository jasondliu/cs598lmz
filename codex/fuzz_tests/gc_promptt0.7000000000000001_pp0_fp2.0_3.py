import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect with destructors
cl = []
def f():
    for i in range(100000):
        obj = C()
        obj.x = 1
        cl.append(obj)
    #print len(gc.garbage), gc.collect()

def f():
    global cl
    for i in range(100000):
        obj = C()
        obj.x = 1
        cl.append(obj)
    cl = []
    #print len(gc.garbage), gc.collect()

def f():
    global cl
    for i in range(100000):
        obj = C()
        obj.x = 1
        cl.append(obj)
    cl = []
    del i
    gc.collect()

def f():
    global cl
    for i in range(100000):
        obj = C()
        obj.x = 1
        cl.append(obj)
    cl = []
    #print len(gc.garbage), gc.collect()
    del i
    gc.collect()

def f():
    global
