import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(a)
del a
del keepalive
gc.collect()
print(lst)

#第一次执行结果：
#['', <__main__.A object at 0x000001E7D4F6F4E0>]
#第二次执行结果：
#['', <__main__.A object at 0x000001E7D4F6F4E0>]
#第三次执行结果：
#['', <__main__.A object at 0x000001E7D4F6F4E0>]
#第四次执行结果：
#['', <__main__.A object at 0x000001E7D4F6F4E0>]
#第五次执行结果
