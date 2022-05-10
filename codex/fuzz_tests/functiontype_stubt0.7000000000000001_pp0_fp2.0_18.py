from types import FunctionType
a = (x for x in [1])
print(type(a))

print(type(lambda x: x))
print(type(FunctionType))
print(type(FunctionType.__call__))
print(type(FunctionType.__call__.__call__))
print(type(FunctionType.__call__.__call__.__call__))


# import types
# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#
# def fn(self, friend):
#     print('Hi, I am %s ...' % self.name)
#     print('My friend is %s ... ' % friend)
#
# Hello = type('Hello', (Person,), dict(sayHello=fn))
#
# h = Hello('Bob', 'male')
# h.sayHello('Tim')


# def fn(self, name='world'): # 先定义函数
#     print('Hello, %s.' % name)
#
# Hello = type('Hello', (object
