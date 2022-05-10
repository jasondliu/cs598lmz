import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
wr=weakref.ref(lst,callback)
keepalive.append(lst)
del lst
print len(keepalive)
import gc
gc.collect()
print wr()
print wr() is None
print len(keepalive)
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
wr=weakref.ref(lst,callback)
keepalive.append(lst)
del lst
print len(keepalive)
import gc
gc.collect()
print wr()
print wr() is None
print len(keepalive)
"""
output:
1
['$H', <__main__.A object at 0x00BECB50>]
True
0
1
['$H', <__main__.A object at 0x00BECB50>]
False
0
"""
"""
3.3.2.2. Testing
