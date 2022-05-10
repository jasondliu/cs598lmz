import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepalive=keepali0e[:]

def test_weak_callback():
    #s=str()
    #r=weakref.ref(s,callback)
    #keepalive.append(r)
    del lst
    gc.collect()
    #assert r() is None

def test_weak_callback_exception():
    #s=str()
    #r=weakref.ref(s,callback)
    #keepalive.append(r)
    #del lst[:]
    #try:
    #    raise ValueError
    #except:
    #    gc.collect()
    #assert r() is None
    pass

def test_finalize_callback():
    #s=str()
    #r=weakref.finalize(s,callback,lst)
    #keepalive.append(r)
    #del lst
    #gc.collect()
    #assert r.alive is False
    pass

def test_finalize_callback_exception():
    #s=
