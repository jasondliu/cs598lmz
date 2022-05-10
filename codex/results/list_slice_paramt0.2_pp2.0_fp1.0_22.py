import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
print lst

#结果：
#['<__main__.A object at 0x7f3d8f8d5f50>']
#['<__main__.A object at 0x7f3d8f8d5f50>']
#['<__main__.A object at 0x7f3d8f8d5f50>']
#['<__main__.A object at 0x7f3d8f8d5f50>']
#['<__main__.A object at 0x7f3d8f8d5f50>']
#['<__main__.A object at 0x7f3d8f8d5f50>']
#['<__main__.A object at 0x7f3d8f8d5f50>']
#['<__main__.A object at 0x7f3d8f8d5f50>']
#['<__main__.A object at 0x7f3d8
