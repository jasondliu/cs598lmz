from types import FunctionType
a = (x for x in [1])

# print(type(a))
# print(dir(a))
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())


def foo(x):
    try:
        print("ok")
        return x
    finally:
        print('--over--')


# print(foo(11))
# print(foo(12))


# 实现一个迭代器
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


# for i in Fibs():
#     if i > 100:
#         break
#     print(i)


# 对迭代器进行包装
class Sqr(object):
    def __init__(self
