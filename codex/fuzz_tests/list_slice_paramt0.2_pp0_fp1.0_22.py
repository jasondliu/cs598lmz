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
#['<__main__.A object at 0x00000000020D9E80>']
#这个结果说明，当a被删除时，a.c指向的对象还存在，所以a.c指向的对象没有被回收
#这个结果说明，当a被删除时，a.c指向的对象还存在，所以a.c指向的对象没有被回收
#这个结果说明，当a被删除时
