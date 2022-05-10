import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print "before del a"
print lst

del a
del a.c

print "after del a"
print lst
#结果：
#before del a
#
#after del a
#

#垃圾回收
#python 使用引用计数来跟踪和回收垃圾。在python内部跟踪着所有使用中的对象以及它们的 计数器。当一个对象被创建时， 就创建了一个引用计数， 当这个对象不再需要时， 也就是说， 这个对象的
