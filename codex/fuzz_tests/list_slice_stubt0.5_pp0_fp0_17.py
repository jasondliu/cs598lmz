import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
lst[0]=a
del lst
gc.collect()
print(keepali0e)

#这里的keepalive是一个list，其中只有一个元素，这个元素是一个A的实例，并且这个实例有一个属性c，这个属性c指向自己。
# 在lst被删除后，lst中的元素被释放，但是这个元素被keepalive持有，所以不会被回收。
# 这里提到的释放元素，指的是
