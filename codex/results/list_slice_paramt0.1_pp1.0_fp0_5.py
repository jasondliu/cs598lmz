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
#['<__main__.A object at 0x7f9b6c0f6a90>']
#这个结果说明，在删除a的时候，a的弱引用被删除了，但是a的引用计数还是1，因为a.c=a，所以a的引用计数还是1，所以a还是存在的

#第二个例子：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback
