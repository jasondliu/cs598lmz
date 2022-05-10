import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A:
#     pass

# a = A()
# print(a.__class__.__name__)

# def get_name(self):
#     return self.__class__.__name__

# import types
# types.MethodType(get_name, a)

# a.get_name = types.MethodType(get_name, a)
# print(a.get_name())

# print(a.get_name)

# class B:
#     def get_name(self):
#         return self.__class__.__name__

# b = B()
# print(b.get_name())

# print(b.get_name)

# class C:
#     def get_name(self):
#         return self.__class__.__name__

# c = C()
# print(c.get_name())

# print(c.get_name)

# class D:
#
