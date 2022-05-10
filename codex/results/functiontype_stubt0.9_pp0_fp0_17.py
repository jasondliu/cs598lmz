from types import FunctionType
a = (x for x in [1])
print(type(a))
#int, bool, str, tuple, list, range, type, object, generator
#int, bool,

a = 1
print(type(a))
print(type(type(a)))
print(type(object))
print(type(type))
print(type(FunctionType))
print(type(int))
print(type(FunctionType))
# -*- coding:utf-8 -*-

class MyType(type):
    def __new__(self,*args,**kwargs):
        print('sdsds', *args)
        return super(MyType,self).__new__(self,*args,**kwargs)
    def __init__(self,name,bases,dict):
        print('----init',name,bases,dict)
        super(MyType,self).__init__(name,bases,dict)
    def __call__(self,*args,**kwargs):
        print('------call',args,kwargs)
        obj = self.__new__(self,args,kwargs
