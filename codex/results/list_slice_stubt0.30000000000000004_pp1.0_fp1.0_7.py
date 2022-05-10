import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#[str(), <weakref at 0x0000021A0B6D5A68; to 'A' at 0x0000021A0B6D5A58>]
#[str()]

#这个例子中，lst是一个列表，它的第一个元素是一个字符串对象，第二个元素是一个弱引用，它引用的是一个A类的实例。
#弱引用的回调函数是callback，它会在引用的对象被回收时被调用，
