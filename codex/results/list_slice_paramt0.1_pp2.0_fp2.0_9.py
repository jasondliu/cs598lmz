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
#['<__main__.A object at 0x0000000003D8D908>']

#结论：
#当一个对象的弱引用被回调函数调用时，该对象的弱引用被从弱引用字典中删除，
#但是该对象的强引用仍然存在，因此该对象不会被垃圾回收。

#结论：
#当一个对象的弱引用被回调函数调用时，该对象
