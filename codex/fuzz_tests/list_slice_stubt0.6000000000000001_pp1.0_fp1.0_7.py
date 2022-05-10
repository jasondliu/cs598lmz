import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(str())
keepalive.append(callback)
w=weakref.ref(a,callback)
del a
print keepalive

# [<__main__.A object at 0x00A1D6F0>, '', <function callback at 0x0164E368>]
# [<__main__.A object at 0x00A1D6F0>, '', <function callback at 0x0164E368>]
# [<__main__.A object at 0x00A1D6F0>, '', <function callback at 0x0164E368>]
# [<__main__.A object at 0x00A1D6F0>, '', <function callback at 0x0164E368>]
# [<__main__.A object at 0x00A1D6F0>, '', <function callback at 0x0164E368>]
# [<__main__.A object at 0x00A1D6F0>, '', <function callback at 0x0164E368>]
# [
