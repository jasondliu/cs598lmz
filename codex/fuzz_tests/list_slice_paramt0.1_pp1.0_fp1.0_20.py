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

#output:
#['<weakref at 0x7f8f9d8c5e18; to 'A' at 0x7f8f9d8c5d50>']

#结论：
#1.当一个对象的引用计数为0时，python会自动删除该对象，并调用该对象的__del__方法
#2.当一个对象的引用计数为0时，python会自动删除该对象，并调用该对象的__del__方法
#3.当一个对象的引用计数为0时，python
