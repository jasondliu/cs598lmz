from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))
# [1, 2, 3]

# 使用元类
class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)

print(list('abc'))
# ['a', 'b', 'c']
print(MyList('abc'))
# ['a', 'b', 'c']
print(MyList('abc')[1])
# (indexing ['a', 'b', 'c'] at 1)
# b
print(MyList('abc')[3])
# (indexing ['a', 'b', 'c'] at 3)
# c

# 元类的一个主要用途就是通过它们去扩
