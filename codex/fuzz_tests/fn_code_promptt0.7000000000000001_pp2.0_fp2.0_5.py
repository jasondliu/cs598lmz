fn = lambda: None
# Test fn.__code__.co_argcount
# fn.__code__.co_varnames = ('x', 'y')

# print(fn.__code__.co_argcount)  # 2
# print(fn.__code__.co_varnames)  # ('x', 'y')

# class A:
#     def __init__(self, x, y):
#         pass

# print(A.__init__.__code__.co_argcount)  # 3

# def sum_all(*args):
#     return sum(args)

# print(sum_all.__code__.co_argcount)  # 1

# def sum_all(x, y):
#     return sum((x, y))

# print(sum_all.__code__.co_argcount)  # 2

# def sum_all(x, *, y):
#     return sum((x, y))

# print(sum_all.__code__.co_argcount)  # 1

# def sum_all(x, y=1
