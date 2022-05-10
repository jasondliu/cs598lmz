import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
print(lst)
del a
print(lst)

#结果：
#['', '']
#['', '']
#这里的结果是因为，在python中，字符串是不可变的，所以，当a被回收时，a.b的弱引用被回收，但是a.b的回调函数没有被调用，所以lst中的第一个元素没有被删除。
#这里的结果是因为，在python中，字符串是不可
