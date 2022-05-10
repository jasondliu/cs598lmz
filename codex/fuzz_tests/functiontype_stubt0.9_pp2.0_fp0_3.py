from types import FunctionType
a = (x for x in [1])
b = isinstance(a, GeneratorType)
c = isinstance(a, IteratorType)
d = isinstance(a, FunctionType)
e = isinstance(a, type(iter([])))
# print(b, c, d, e)


# iter(): 把传入的参数变为一个迭代器
# from types import FunctionType
# my_list = [1, 5, 2, 0, 9]
# print(isinstance(iter(my_list), IteratorType))


# next(iter): 迭代器的方法，和普通变量直接读取是一样的(但是会自动到下一项)
# my_list = [1, 5, 2, 0, 9]
# my_iter = iter(my_list)
# a = next(my_iter)
# b = next(my_iter)
# c = next(my_
