from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = 'abc'
e = 1,
f = {1:1}
g = 1
h = FunctionType(lambda : None, globals())

# print(a.__dict__)
# print(b.__dict__)
# print(c.__dict__)
# print(d.__dict__)
# print(e.__dict__)
# print(f.__dict__)
# print(g.__dict__)
# print(h.__dict__)  # 这个有 __defaults__ 和 __kwdefaults__
print(str.__dict__)  # 这个有 mro 属性

# 方法 __get__ 和 __set__
class MyDescriptor:
    def __get__(self, instance, owner):
        print(instance, owner)

    def __set__(self, instance, value):
        print(instance, value)


class Test
