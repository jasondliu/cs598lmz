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
print(lst)

#结果
#[str(), <weakref at 0x000002B5D8A0E948; to 'A' at 0x000002B5D8A0E898>]

#可以看到，在删除a的时候，没有调用callback函数，这是因为a还有一个引用，就是a.c=a，这个引用是循环引用，所以不会被回收
#因此，在使用弱引用的时候，要注意循环引用的问题

#
