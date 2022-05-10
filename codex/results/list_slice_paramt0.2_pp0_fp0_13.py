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

#结果：
#['<__main__.A object at 0x0000000003C7A5F8>']

#结论：
#在python中，循环引用不会导致内存泄露，因为python的垃圾回收机制会自动清理循环引用的对象。
#但是，循环引用会导致引用计数永远不为0，从而导致垃圾回收机制不会回收这些对象，从而导致内存占用一直增
