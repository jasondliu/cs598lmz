import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(a)
del a
lst.append(a)
print keepalive
print lst
print len(lst)
lst.pop() #长度减小
print keepalive
print lst
print len(lst)
lst.pop()
print keepalive
print lst
print len(lst)
lst.pop()
print keepalive
print lst
print len(lst)
lst.pop()
print keepalive
print lst
print len(lst)
lst.pop()
print keepalive
print lst
print len(lst)
"""
#测试自定义类型的异常抛出
"""
import re
import time
class myException(Exception):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "myException:%s"%(self.name)
   
