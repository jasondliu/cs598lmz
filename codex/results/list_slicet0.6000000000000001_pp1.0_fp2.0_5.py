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
print(keepali0e)

#解析
#1、程序必须有引用链，否则就不会调用回调函数
#2、回调函数必须是可调用的，且不能有参数
#3、回调函数的参数值必须是可哈希的。
#4、回调函数的参数值必须是可哈希的，因此回调函数的参数值不能是列表，不能是字典，不能是集合，不能是自定义的类的实
