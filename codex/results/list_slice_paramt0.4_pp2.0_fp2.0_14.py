import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
print len(lst)
del a
print len(lst)
del lst
print keepali0e[0]()

'''

def test():
    import gc
    l=[]
    l.append(l)
    gc.collect()
    print gc.garbage

def test1():
    import gc
    gc.disable()
    l=[]
    l.append(l)
    gc.collect()
    print gc.garbage

def test2():
    import gc
    gc.enable()
    l=[]
    l.append(l)
    gc.collect()
    print gc.garbage

def test3():
    import gc
    gc.set_debug(gc.DEBUG_STATS)
    l=[]
    l.append(l)
    gc.collect()
    print gc.garbage

def test4():
    import gc

