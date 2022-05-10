import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive=weakref.ref(a,callback)
print(lst)
del a
del keepa1ive
del keepalive
print(lst)

#答案：
#['<__main__.A object at 0x0000020A3C7F4F60>']
#[]

#-------------------------------------------------------------------------
#第十六题
#下面的代码输出什么？
#def f(x,l=[]):
#    for i in range(x):
#        l.append(i*i)
#    print(l)
#f(2)
#f(3,[3,2,1])
#f(3)
#答案：
#[0, 1]
#[3, 2, 1, 0, 1, 4]
#[0, 1, 0, 1, 4]

#-------------------------------------------------------------------------
#第十七题
#
