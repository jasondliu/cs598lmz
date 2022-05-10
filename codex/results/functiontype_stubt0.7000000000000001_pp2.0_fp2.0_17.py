from types import FunctionType
a = (x for x in [1])
a.__name__

b = FunctionType(lambda x: x, globals())
b.__name__

# class NameTest:
#     def __init__(self, name):
#         self.name = name
#
#     def __get__(self, instance, owner=None):
#         return self.name
#
#     def __set__(self, instance, value):
#         self.name = value
#
#     def __delete__(self, instance):
#         pass
#
#     def __set__(self, instance, value):
#         self.name = value
#
#     def __delete__(self, instance):
#         pass
#
#
# class Descriptor(object):
#     def __init__(self):
#         self.name = 'Descriptor'
#
#     def __get__(self, instance, owner):
#         return self.name
#
#     def __set__(self, instance, value):
#         self.name = value
#
#     def __delete__(
