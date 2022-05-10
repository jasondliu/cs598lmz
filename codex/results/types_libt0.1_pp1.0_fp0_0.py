import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A(object):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# a = A('a')
# print(a.get_name())
#
#
# def get_name(self):
#     return self.name
#
#
# A.get_name = get_name
#
# print(a.get_name())
#
#
# def get_name(self):
#     return self.name + '1'
#
#
# A.get_name = get_name
#
# print(a.get_name())
#
#
# def get_name(self):
#     return self.name + '2'
#
#
# a.get_name = types.MethodType(get_name, a)
#
# print(a.get_name())
#
#
# def get_
