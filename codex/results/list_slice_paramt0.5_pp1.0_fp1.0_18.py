import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]

# __del__()函数
class A(object):
	def __init__(self,name):
		self.name=name
	def __del__(self):
		print '%s is dead.' % self.name

a=A('a')
b=A('b')
del a
del b

# 元类
type(type)
type(object)
type(str)
type(int)

type('a')
type(1)

type('type',(object,),{})
type('type',(type,),{})

# type实例化
def add(self,other):
	return self.a+other.a

A=type('A',(object,),{'a':1,'add':add})
a=A()
b=A()
a.add(b)

# 元类实例化
def upper_attr(future_class_name,future_class
