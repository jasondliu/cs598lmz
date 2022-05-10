import types
types.MethodType(lambda self: self.__class__.__name__, None, object)

# class A:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def __repr__(self):
#         return self.name
#
#     def __getattr__(self, item):
#         return item
#
#     def __getattribute__(self, item):
#         return item
#
#     def __setattr__(self, key, value):
#         print(key, value)
#
#     def __delattr__(self, item):
#         print(item)
#
#     def __call__(self, *args, **kwargs):
#         print(args, kwargs)
#
#     def __len__(self):
#         return 1
#
#     def __getitem__(self, item):
#         return item
#
#     def __setitem__(self, key,
