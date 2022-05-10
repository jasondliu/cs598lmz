import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive=a
print lst,id(lst)
del a
print lst,id(lst)
print len(lst)
print lst[0],lst[0].c
lst[0]=1
print len(lst)
lst[0]=2
lst[0]=4
lst[0]=6
lst[0]=8
lst[0]=10
print lst,id(lst)
lst[0]=12
print id(lst)
lst[0]=14
lst[0]=16
lst[0]=18
lst[0]=20
lst[0]=22
lst[0]=24
lst[0]=26
lst[0]=28
lst[0]=30
lst[0]=32
lst[0]=34
lst[0]=36
lst[0]=38
lst[0]=40
lst[0]=42
lst=[]
print len(lst)
lst[0]=44

