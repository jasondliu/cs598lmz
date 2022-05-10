import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print lst

#[str(), <weakref at 0x00000000022F8D08; to 'A' at 0x00000000022F8C88>]
#[str()]

#第一次打印的时候，lst中有两个元素，一个是str()，一个是weakref对象，
#第二次打印的时候，因为a被删除，所以weakref对象被回调函数删除了，所以lst中只剩下str()

#weakref.ref(object[,callback])
#创建一个弱引用，
