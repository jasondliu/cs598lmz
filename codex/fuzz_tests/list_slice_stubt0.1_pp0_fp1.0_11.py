import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
gc.collect()
print(lst)

#结果：
#['', <__main__.A object at 0x000002A9D7D9E898>]
#这里的a.c=a，是一个循环引用，所以a不会被回收，但是lst[0]被回收了，所以lst[0]变成了一个空字符串。
#这里的lst[0]是一个空字符串，所以lst[0]被回收了，所以lst[0]变成了一个空字符串。
#这里
