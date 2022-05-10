import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a ;b=A();b.c=a
keepali0e.append(a)
keepali0e.append(b)
weakref.ref(b,callback)
weakref.ref(b.c,callback)
del a ; del b
if __name__=="__main__":
    import gc;gc.set_debug(gc.DEBUG_UNCOLLECTABLE)
