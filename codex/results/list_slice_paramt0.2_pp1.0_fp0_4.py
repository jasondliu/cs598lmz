import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#结果：['\x00']

#结论：
#1.当一个对象的弱引用被删除时，调用回调函数
#2.当一个对象的弱引用被删除时，该对象的弱引用被删除
#3.当一个对象的弱引用被删除时，该对象的弱引用被删除，但是该对象的强引用不会被删除
#4.当一个对象的弱引用
