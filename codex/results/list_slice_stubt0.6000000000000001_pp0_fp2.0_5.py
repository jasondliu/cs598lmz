import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
print(lst)
del a
print(lst)

#垃圾回收触发条件
#可达性分析：
#1.引用计数
#2.根对象
#3.循环引用
#4.弱引用

#根对象
#1.导入的模块
#2.全局变量
#3.自己创建的
import module
print(module.__dict__)
#全局变量
global_var=[]
print(globals())
#自己创建的
class A(object):pass
a=A()
print(a.__dict__)

#循环引
