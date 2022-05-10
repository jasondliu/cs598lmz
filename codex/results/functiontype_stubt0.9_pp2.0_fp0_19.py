from types import FunctionType
a = (x for x in [1])
a() = 123

# b = {}
# b() = 123

# callable(a)

# class A(dict):
#     def __getitem__(self, item):
#         return 123
# c = A()
# c[1][2] = 123

# a = (1, 2)
# a[0] = 123


# class A:
#     def __getitem__(self, item):
#         return 123
# c = A()
# c[1] = 123


# class A:
#     def __setitem__(self, item, value):
#         # print(item,value)
#         super().__setitem__(item, value)
#     def __getitem__(self, item):
#         # print(item)
#         return super().__getitem__(item)
# c = A()
# print(c[1])


a = [1, 2]
try:
    a[0] = 123
except TypeError as e:
    print(e)
# a[1][
