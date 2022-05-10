import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(a)
lst.append(a)
keepali0e.append(weakref.ref(a,callback))
del a
del lst
while keepali0e[0]():pass
print lst

#结果：
# ['', <__main__.A object at 0x1004d7a50>, <__main__.A object at 0x1004d7a50>, <__main__.A object at 0x1004d7a50>]
# ['', <__main__.A object at 0x1004d7a50>, <__main__.A object at 0x1004d7a50>]
# ['', <__main__.A object at 0x1004d7a50>]
# []
# 由于lst和a引用了同一个引用计数为3的对象，所以lst删除一个引用
