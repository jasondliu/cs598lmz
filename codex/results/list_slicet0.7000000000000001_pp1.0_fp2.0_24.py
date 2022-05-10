import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
 
#经典算法
#定义栈类
class Stack(object):
 def __init__(self,size=0x10):
  self.stack=[]
  self.size=size
 def push(self,value):
  self.stack.append(value)
 def pop(self):return self.stack.pop()
 def top(self):return self.stack[-1]
 def is_empty(self):return not bool(self.stack)
 def is_full(self):return len(self.stack)>=self.size

#逆波兰表达式
class Calculator(object):
 def __init__(self,formula):
  self.stack=Stack()
  self.formula=formula.split()
 #根据运算符进行计算
 def calculate(self,operator):
  right=self.stack.pop()
  left=self.stack.pop()
  if operator=='+':return
