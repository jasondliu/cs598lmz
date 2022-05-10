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

#结果：['\x00']

#问题：为什么是['\x00']？

#解答：
#创建一个A类的实例a，然后将a赋值给a.c，这样a.c引用了a，a又引用了a.c，所以a和a.c形成了循环引用。
#然后创建一个弱引用对象，弱引用对象引用了a，并且指定回调函数callback。
#删除a后，a和
