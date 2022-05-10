import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=a
d=a.d=A()
d.c=d
d.a=d.b=lst[0]
keepali0e.append([lst,a,d])
del a,d
try:
    import gc
    gc.collect()
except:
    for x in range(4):
        for y in range(5):
            __import__('test.test_descr').descr_misc.callback(None)
