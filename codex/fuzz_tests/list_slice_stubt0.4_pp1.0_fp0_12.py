import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
gc.collect()
print(len(lst))

#结果：0
#分析：
#1.创建一个A类，创建一个回调函数，创建一个空列表
#2.创建一个空字符串，添加到lst列表中，创建一个A类的实例，将这个实例添加到keepalive列表中
#3.删除A类的实例，执行垃圾回收，打印lst列表的长度
#4.结果
