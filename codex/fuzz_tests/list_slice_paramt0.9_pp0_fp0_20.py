import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst))
keepali0e.append(weakref.ref(str))
lst=None
#此时lst未引用，但a由于循环引用导致c对象不会被垃圾回收
#故此时全局对象中的a、c、str()不会被回收
#故此时全局对象的都不会被回收，但是lst引用的内存却被回收了
gc.collect()
print "----------------"
print keepali0e
print a.c is a
#此时只有在回调函数中将c删除后
print g
