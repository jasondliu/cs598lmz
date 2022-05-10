from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

print("==================")

# generator 作为一个迭代器
def square_list(list_data):
    for x in list_data:
        yield x*x

my_list = [1,2,3,4]
generator = (x*x for x in my_list)
for i in generator:
    print(i)

print("==================")

# generator 作为一个函数
def gen_func(list_data):
    for x in list_data:
        yield x*x

my_list = [1,2,3,4]
for i in gen_func(my_list):
    print(i)

print("==================")

# generator 作为一个函数，可以使用 next() 函数
def gen_func(list_data):
    for x in list_data:
        yield x
