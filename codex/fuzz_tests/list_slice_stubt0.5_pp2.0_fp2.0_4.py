import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(callback)
keepalive.append(lst)
del keepalive
"""
    def test_weakref_callback_with_del(self):
        def callback(x):
            del lst[0]
        lst = [str()]
        r = weakref.ref(lst, callback)
        del lst
        self.assertRaises(IndexError, r)

    def test_weakref_callback_with_set(self):
        def callback(x):
            lst[0] = None
        lst = [str()]
        r = weakref.ref(lst, callback)
        del lst
        self.assertIsNone(r())

    def test_weakref_callback_with_pop(self):
        def callback(x):
            lst.pop()
        lst = [str()]
        r = weakref.ref(lst, callback)
        del lst
        self.assertRaises(IndexError, r)

    def test_weakref
