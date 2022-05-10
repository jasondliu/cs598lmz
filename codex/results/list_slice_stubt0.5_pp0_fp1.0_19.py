import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
a=None
keepalive.append(lst)
del lst
import gc
for i in range(4):gc.collect()
print(keepalive)

#结果
#[['', <__main__.A object at 0x000001A0D0A7A898>], ['', <__main__.A object at 0x000001A0D0A7A898>]]
#[['', <__main__.A object at 0x000001A0D0A7A898>]]
#[['', <__main__.A object at 0x000001A0D0A7A898>]]
#[['', <__main__.A object at 0x000001A0D0A7A898>]]
#[['', <__main__.A object at 0x000001A0D0A7A898>]]
#[['', <__main__.A object at 0x000001A0D0A
