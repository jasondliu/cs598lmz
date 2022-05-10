import types
# Test types.FunctionType type
def test_fun():
    pass

# print(type(test_fun))
# print(type(abs))
# print(type(lambda x:  x))
# print(type(x for x in range(10)))

# Test types.GeneratorType type
# g = (x for x in range(10))
# print(type(g))

# Test types.LambdaType type
# f = lambda x:  x
# print(type(f))


# Test types.BuiltinFunctionType type
# print(type(abs))

# Test types.BuiltinMethodType type
# print(type(str.capitalize))
# print(type([].append))

# Test types.MethodType type
# from types import MethodType
#
#
# class Student(object):
#     pass
#
#
# s = Student()
# print(s.name)
#
#
# def set_age(self, age):
#     self.age = age
#
#
# s.set_age = MethodType(set_age,
