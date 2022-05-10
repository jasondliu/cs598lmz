from types import FunctionType
list(FunctionType(code,globals(),'f'))

#使用exec执行代码
# exec(code,globals())
# f(2)

#使用types模块定义函数
# import types
# def greet(name):
#     print('hello',name)
#
# greet('jack')
#
# greet2=types.FunctionType(greet.__code__,greet.__globals__,name='greet2',argdefs=(),closure=())
#
# greet2('john')
#
# print(greet2.__code__)
# print(greet2.__code__.co_varnames)
# print(greet2.__code__.co_argcount)

#使用__new__方法创建对象

# import  weakref
# class CarModel:
#     _models=weakref.WeakValueDictionary()
#     def __new__(cls,model_name,*
