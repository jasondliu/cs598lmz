import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.lst=lst
a.keepalive=keepalive
a.callback=callback
keepalive.append(a)
lst.append(a)
a.callback(lst)
""", """
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.lst=lst
a.keepalive=keepalive
a.callback=callback
keepalive.append(a)
lst.append(a)
a.callback(lst)
""")

    def test_gc_collect_list_with_callback(self):
        self.run_test("""
import gc
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.lst=lst
a.keepalive=keepalive
a
