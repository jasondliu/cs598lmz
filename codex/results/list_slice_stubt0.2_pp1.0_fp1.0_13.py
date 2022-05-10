import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
del a
gc.collect()
print(lst)

#结果：
#[<__main__.A object at 0x000002A0D6B0B5F8>]
#[<__main__.A object at 0x000002A0D6B0B5F8>]
#[<__main__.A object at 0x000002A0D6B0B5F8>]
#[<__main__.A object at 0x000002A0D6B0B5F8>]
#[<__main__.A object at 0x000002A0D6B0B5F8>]
#[<__main__.A object at 0x000002A0D6B0B5F8>]
#[<__main__.A object at 0x000002A0D6B0B5F8>]
#[<__main__.A object at 0x000002A0D6B0B5F8>]
#[<__
