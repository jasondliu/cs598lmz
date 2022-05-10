import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#output:
#['<__main__.A object at 0x7f7c9c0>']

#结论：
#1.当一个对象的引用计数为0时，它会被垃圾回收，但是如果它有弱引用，那么它会被放入垃圾回收器的待回收队列中，
#  当垃圾回收器运行时，它会检查待回收队列中的对象，如果对象的引用计数为0
