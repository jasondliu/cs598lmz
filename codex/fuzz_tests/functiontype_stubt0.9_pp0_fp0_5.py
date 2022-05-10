from types import FunctionType
a = (x for x in [1])
print(a.__next__())
for value in a:
    print(value)
# b = (x for x in range(10))
# for value in b:
#     print(value)

print(type(a))

# c = "abcd"
# print(type(c) == StringType) #判断变量类型
# print(type(FunctionType))
# print(type(str) == type(FunctionType))

# print(isinstance(a, Iterable))
# print(isinstance(a, Iterator))
# print(isinstance(b, Iterable))
# print(isinstance(b, Iterator))

# print(dir(a))

# for i,value in enumerate([1,2,3,4]):
#     print(i,value)

# for x,y in [(1,4),(4,5),(7,8)]:
#     print(x,y)

# def f(a,b):
#     print(a,b)

