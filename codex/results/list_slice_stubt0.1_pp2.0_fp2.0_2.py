import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst.append(weakref.ref(lst,callback))
del lst
print(keepalive)

#结果：
#[<__main__.A object at 0x000002A7E8B8F908>]
#这里的结果是因为lst是一个列表，列表中有两个元素，一个是字符串，一个是弱引用，
# 当删除lst的时候，列表中的字符串被删除，弱引用没有被删除，因为弱引用中的回调函数
# 删除了列表
