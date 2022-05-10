import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
a.c=lst
weakref.ref(a,callback)
del a,keepalive

#利用weakref构造循环引用的数据结构
import weakref
class Data(object):
    def __init__(self,value,owner):
        self.value=value
        self.owner=weakref.ref(owner)
    def __str__(self):
        return '%s '%self.owner()
class Node(object):
    def __init__(self,value):
        self.data=Data(value,self)
    def __del__(self):
        print('in Node.__del__')
    def __str__(self):
        return '%s'%self.data
a=Node('a')
b=Node('b')
a.data.owner=b
b.data.owner=a
del a,b

#对象的弱
