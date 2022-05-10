from types import FunctionType
a = (x for x in [1])
# a.send(2)
print("a是生成器")
b = FunctionType
print("b 是函数")
c = lambda x: x ** 2
# # print("c 是"+c.__name__)
print("c 是匿名函数" if c.__name__ == "<lambda>" else "c 不是匿名函数")
d = yield 1
print("d是协程")

# def say_hello(name):
#     return lambda : print("hello,",name)
#
#
# hello = say_hello("JuJu")
# hello()
# hello.__name__


# import math
# import functools
#
#
# class MyClass:
#     @staticmethod
#     def say_hello():
#         print("你好")
#
#
# MyClass.say_hello()
#
# a = [x for x in range(100)]
# print(list(map(math.sqrt,
