import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#结果
#['<__main__.A object at 0x000001A6A0B6C908>']
#[]

#结论
#当一个对象的引用计数为0时，python解释器会调用对象的__del__方法，然后释放对象占用的内存。
#当一个对象的引用计数为0时，python解释器会调用对象的__del__方法，然后释放对象占用的内存。
#当一个对象的引用
