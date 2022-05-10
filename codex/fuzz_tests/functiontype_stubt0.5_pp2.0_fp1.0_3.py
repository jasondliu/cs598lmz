from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.__next__.__call__))
print(type(a.__next__.__call__.__call__))
print(type(a.__next__.__call__.__call__.__call__))
print(type(a.__next__.__call__.__call__.__call__.__call__))
print(type(a.__next__.__call__.__call__.__call__.__call__.__call__))
print(type(a.__next__.__call__.__call__.__call__.__call__.__call__.__call__))
print(type(a.__next__.__call__.__call__.__call__.__call__.__call__.__call__.__call__))

# class A:
#     def __init__(self):
#         self.a = 0
#
#     def __call__(self, *
