from types import FunctionType
a = (x for x in [1]) # generator
print(isinstance(a, GeneratorType))
b = {1} # set
print(isinstance(b, Set))
c = [] # list
print(isinstance(c, list))
print(isinstance(len, FunctionType))
d = 1/2 # float
print(isinstance(d, (int, float)))
print(type(d), type(len), type(b), type(c), type(a), type(print), type(FunctionType), type(GeneratorType))

print(dir(dict))
print(len.__doc__)
print(print.__doc__)
print(print.__name__)
print(igetattr(dict, 'pop')) # dict.pop

# 9. 凡是可作用于 for 循环的对象都是 Iterable 类型；
# 
# 凡是可作用于 next() 函数的对象都是 Iterator 类型，
