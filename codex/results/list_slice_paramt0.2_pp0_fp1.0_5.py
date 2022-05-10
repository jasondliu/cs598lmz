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
#['<__main__.A object at 0x7f7d6d8b6c50>']
#可以看到，当a被删除时，a的弱引用被删除，这时候回调函数被调用，但是回调函数中的del lst[0]并没有被执行，这是因为a的弱引用被删除时，a还没有被回收，因此回调函数中的del lst[0]没有执行。

#第二个例子：
