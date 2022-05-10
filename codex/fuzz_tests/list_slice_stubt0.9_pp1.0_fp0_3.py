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
reduce(dir)
del lst[0]
lst[0]=[A()]
lst[0][0].c=lst[0][0]
fw=weakref.ref(lst[0][0],callback)
for i in range(11):
    del lst[0][0]
    lst[0][0:0]=[A()]
    del lst[0][0]
    lst[0][0:0]=[A()]
    lst[0][0]=2
    del lst[0][0]
    lst[0][0:0]=[2]
    del lst[0][0]
    lst[0]=[]
    lst[0][0:0]=[A()]
    del lst[0
