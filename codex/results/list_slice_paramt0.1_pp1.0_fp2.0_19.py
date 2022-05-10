import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#结果：
#['<__main__.A object at 0x0000000003D7A9B0>']
#['<__main__.A object at 0x0000000003D7A9B0>']
#['<__main__.A object at 0x0000000003D7A9B0>']
#['<__main__.A object at 0x0000000003D7A9B0>']
#['<__main__.A object at 0x0000000003D7A9B0>']
#['<__main__.A object at 0x0000000003D7A9B0>']
#['<__main__.A object at 0x0000000003D7A9B0>']
#['<__main__.A object at 0x0000000003D7A9B0>']
#['<__main__.A object at 0x0000000003D7A9B0>']
#['<__main__.A object at 0x0000000003
