import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print('lst:',lst)
del a
print('lst:',lst)

#这个例子与前一个例子不一样，这里的闭包是一个弱引用，它不会对对象进行强引用。
#当删除对象的引用的时候，回调被调用，并删除列表中的对象。

"""
>>> import weakref
>>> class A(object):
...     pass
...
>>> a=A()
>>> weak = weakref.ref(a)
>>> weak
<weakref at 0x020152C8; to 'A' 
at 0x020150A0>
>>> weak()
<__main__.A object at 0x020150D0>

