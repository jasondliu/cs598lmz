from types import FunctionType
a = (x for x in [1])
a.__next__()
dir(a)
# help(a)
b = a
a.__next__()
b.__next__()
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# c = [1,2,3]
# d = c
# c.append(4)
# print(d)

# e = [1,2,3]
# f = [1,2,3]
# e is f
# e == f

# g = [1,2,3]
# h = g
# g == h
# g is h

# i = [1,2,3]
# j = [1,2,3]
# i == j
# i is j

# k = (1,2,3)
# l = (1,2,3)
# k == l
# k is l

# m = (1,2,3)
# n = m
# m == n
