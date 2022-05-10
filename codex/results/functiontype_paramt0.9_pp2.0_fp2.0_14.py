from types import FunctionType
list(FunctionType(lambda x: x*x, globals())(3))

num_list = [1, 2, 3]
squared_ints = list(map(lambda x: x * x, num_list))
print(squared_ints)

squared_ints = [x * x for x in num_list]
print(squared_ints)

squared_ints = list(map(lambda x: x * x, filter(lambda x: x > 1, num_list)))
print(squared_ints)

squared_ints = [x * x for x in num_list if x > 1]
print(squared_ints)
