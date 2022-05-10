import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print len(lst)
del a
print len(lst)

#output:
#2
#1

#第一个输出是因为lst中有两个元素，一个是字符串，一个是弱引用对象
#第二个输出是因为当a被删除时，a的弱引用对象被回调函数删除了，所以lst中只剩下字符串了

#结论：
#1.弱引用对象不会增加引用计数
#
