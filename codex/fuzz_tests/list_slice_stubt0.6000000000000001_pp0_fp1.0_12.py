import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive=[]
keepalive.append(weakref.ref(lst[0],callback))
del a
del lst
print len(keepalive)
print len(keepali0e)



#tuple
#tuple是另一种有序列表叫元组，和列表一样，元组用()标识，内部元素用逗号隔开
#元组中的元素类型也可以不相同
#元组在初始化时，需要在元素后面添加逗号，否则括号会被当做运算符号使用
#元
