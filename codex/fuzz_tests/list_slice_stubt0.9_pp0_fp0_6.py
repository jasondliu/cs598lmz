import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.ref=weakref.ref(a,callback)
b=A()
b.ref=weakref.ref(b,callback)
keepalive.append(lst)
keepalive.append(a)
keepalive.append(b)
a=None
b=None
#对象的引用计数减一，为0时，垃圾回收器会调用callback回调函数，删除lst列表的第一个元素，也就是lst[0]='test'，
#但由于lst列表没有被销毁，还会和lst[0]还存在一个索引0的引用，这就使得lst引用
