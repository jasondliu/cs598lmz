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
#在回调里面删除列表的第一个元素
#用weakref.ref引用了A的实例
#在删除a的时候，会调用callback函数
