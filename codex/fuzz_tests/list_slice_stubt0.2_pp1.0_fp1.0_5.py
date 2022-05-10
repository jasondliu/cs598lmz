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

# [<__main__.A object at 0x7f8c6f9d6a90>]
# [<__main__.A object at 0x7f8c6f9d6a90>]
# [<__main__.A object at 0x7f8c6f9d6a90>]
# [<__main__.A object at 0x7f8c6f9d6a90>]
# [<__main__.A object at 0x7f8c6f9d6a90>]
# [<__main__.A object at 0x7f8c6f9d6a90>]
# [<__main__.A object at 0x7f8c6f9d6a90>]
# [<__main__.A object at 0x7f8c6f9d6a90>]
# [<__main__.A object at 0x7f
