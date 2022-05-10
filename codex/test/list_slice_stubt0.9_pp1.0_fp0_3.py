import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
fw=weakref.ref(lst[0],callback)
for i in range(10):
    lst.append(str())
    lst[-2]=lst[-1]
    lst[-1]=str()
del a
