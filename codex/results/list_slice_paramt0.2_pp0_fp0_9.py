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
#['<weakref at 0x7f2d5c0b4e88; to 'A' at 0x7f2d5c0b4e48>']

#第二种情况：
#当一个对象的弱引用被回调函数调用时，这个对象的弱引用被删除，但是这个对象的强引用仍然存在，
#那么这个对象的弱引用不会被回调函数调用。
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]

