import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]
"""

# addlibs.py
#
# libs.append(sharedlibname) and libs.remove(sharedlibname)
#
TEST_ADD_LIBS = """
import weakref
class A(object): pass
def callback(x):
    del lst[0]
keepalive = []
lst = [str()]
a = A()
a.c = a
keepalive.append(weakref.ref(a, callback))
lst[0]
"""

# badoo.py
#
# Out-of-bounds string access
#
TEST_BADOO = """
class A(object):
    def __getitem__(self, index):
        s = '%s'
        return s[index * 2**31]
triggered_error = False
try:
    A()[42]
except IndexError:
    triggered_error = True
triggered_error
"""

# badpypy.py
#
# Segmentation fault
#
T
