from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(type(a))
print(type(b))
print(a is b)
c = (y for y in [5])
d = c
# print(d is c)
print(type(d))
print(isinstance(a, GeneratorType))
print(isinstance(type(a), type))
print(isinstance(str, object))
print(isinstance('a', object))
print(type(object))
print(FunctionType)
print(type(lambda x: x))
print(type(lambda x: x) == FunctionType)
print(isinstance(lambda x: x, FunctionType))
print(isinstance(c, GeneratorType))
print(issubclass(bool, int))


# 测试behave框架

# login = FeatureLoader('/home/mi/PycharmProjects/Lemon/auto_test/test_B/Steps folder')
#
# with login:
#     login.run()
