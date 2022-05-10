import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
weakref.ref(lst,callback)
del a
del keepalive[:]
lst[0]
print(lst)

# 打印结果：
# ['', <__main__.A object at 0x000001B9B8F8E7B8>]
# ['', <__main__.A object at 0x000001B9B8F8E7B8>]
# ['', <__main__.A object at 0x000001B9B8F8E7B8>]
# ['', <__main__.A object at 0x000001B9B8F8E7B8>]
# ['', <__main__.A object at 0x000001B9B8F8E7B8>]
# ['', <__main__.A object at 0x000001B9B8F8E7B8>]
# ['', <__main__.A object at 0x000001B9B8F8E7B8
