import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
print len(lst)
for x in range(4):print lst
del a

import gc
gc.collect()
print "gc.collect():",len(lst),";","gc.collect():",g.garbage
obj=g.garbage[0]
obj.attri
 
    
a=A()
a.attr1=1
a.attr2=2
a.attr3=3
keepali0e.append(a)
a=None
print len(lst)
for x in range(4):print lst
del a


# 弱引用和生命周期解析器的实例
import weakref
class A(object):pass
a=A()
a.attr1=1
a.attr2=2
a.attr3=3
b=WeakKeyDictionary()
c=WeakValueDictionary()
b['a'] ,c['b'] =1,2
key_callback=c.weakkey_
