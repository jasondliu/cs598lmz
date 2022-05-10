import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
keepalive=a
del a
while keepalive:del lst
del keepalive
'''
    def test_weakref_destroy_callback(self):
        def callback(x):
            del lst[0]
        keepalive = []
        lst = [str()]
        a = A()
        a.c = a
        lst.append(weakref.ref(a, callback))
        keepalive = a
        del a
        while keepalive:
            del lst
            del keepalive

    def test_weakref_create_cycle_with_callback(self):
        def callback(x):
            del lst[0]
        keepalive = []
        lst = [str()]
        a = A()
        a.c = a
        lst.append(weakref.ref(a, callback))
        lst.append(weakref.ref(a, callback))
        keepalive = a
        del a
        while keepalive
