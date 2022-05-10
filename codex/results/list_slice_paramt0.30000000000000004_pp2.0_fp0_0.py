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

#output:
#['<__main__.A object at 0x00000000029D6F60>']

#第二次运行
#output:
#['<__main__.A object at 0x00000000029D6F60>']

#第三次运行
#output:
#['<__main__.A object at 0x00000000029D6F60>']

#第四次运行
#output:
#['<__main__.A object at 0x00000000029D6F60>']

#第五次运行
#output:
#['<__main__.A object at 0x00000000029D6F60>']

#第六次运行
#output:
#['<__main__.A object at 0x00000000029D6F60>']

#第七次运
