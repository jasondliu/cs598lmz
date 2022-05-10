import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]="test"
a=None

"""
def test_ref_callback():
    import sys,weakref
    class A(object):
        pass
    def callback(x):
        print "callback:",x
    a=A()
    a.c=a
    r=weakref.ref(a,callback)
    a=None
    print "callback not called yet"
    sys.stdout.flush()
    import gc; gc.collect()
    print "callback called"

def test_ref_callback_with_exc():
    import sys,weakref
    class A(object):
        pass
    def callback(x):
        print "callback:",x
        raise RuntimeError
    a=A()
    a.c=a
    r=weakref.ref(a,callback)
    a=None
    print "callback not called yet"
    sys.stdout.flush()
    import gc; gc.collect()
    print "callback called"

def test_ref_callback_with_
