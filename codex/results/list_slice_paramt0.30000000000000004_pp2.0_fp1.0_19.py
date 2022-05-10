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

#输出结果
#['<weakref at 0x0000000002B0D6C8; to 'A' at 0x0000000002B0D6D8>']

#解释
#这个例子中，a.c=a，导致a对象存在引用循环，因此a对象不会被垃圾回收。
#但是，a对象的弱引用对象a.c被添加到了lst列表中，因此a.c变成了强引用，
#所以a对象被强引用，不会被垃圾回
