import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(keepali0e)

#输出:
#[<weakref at 0x00000000025D5E08; dead>, <weakref at 0x00000000025D5E48; dead>, []]
#结论:
#当callback被调用时,lst[0]被删除,lst变成空列表,while循环结束

#实例3:
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(keepali0e)

#输出:
#[<weakref at 0x00000000025D5E08; dead>, <weakref at 0x
