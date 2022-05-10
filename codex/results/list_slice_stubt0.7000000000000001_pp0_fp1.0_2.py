import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a=None
#print(len(lst))
lst[0]='cb'
#print(len(lst))
lst[0]=weakref.ref(lst,callback)
#print(len(lst))
del lst
#print(len(lst))

#动态类型
a=None
#print(type(a))
a=3
#print(type(a))
a='abc'
#print(type(a))

#对象引用
a=[1,2,3]
b=a
#print(a is b)
a=None
#print(a)
#print(b)
#print(b is None)

#浅拷贝
#print('浅拷贝')
a=[[1,2],[3,4]]
b=a[:]
#print(a)
#print(b)
#print(a[0] is b[0])
#print
