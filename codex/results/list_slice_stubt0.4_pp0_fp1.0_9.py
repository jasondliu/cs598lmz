import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del keepalive[:]

#结果：
#lst[0] is str()
#lst[1] is <weakref at 0x7f0f5d5a5c70; to 'A' at 0x7f0f5d5a5c10>
#lst[1]() is <__main__.A object at 0x7f0f5d5a5c10>
#lst[1]() is <__main__.A object at 0x7f0f5d5a5c10>
#lst[1]() is <__main__.A object at 0x7f0f5d5a5c10>
#lst[1]() is <__main__.A object at 0x7f0f5d5a5c10>
#lst[1]() is <__main__.A object at 0x7f0f5d5a5c10>
#
