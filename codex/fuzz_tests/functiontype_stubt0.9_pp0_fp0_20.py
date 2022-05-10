from types import FunctionType
a = (x for x in [1])
b = lambda x:x+1 in a
# b为生成器表达式，a为list中的生成器
assert type(b) == FunctionType
print(b())

# 列表解析
odds = [x for x in range(10) if x%3 == 2]
print(odds)
print([n*n for n in range(10)])
print({i: chr(65+i) for i in range(26)})
print({i: 0 for i in range(10)})

# all用于判断所有元素都为真, or用于判断有一个元素为True
# 所有返回值为True的对象，all都会返回True
print(all([1, 2, 3]))
print(all([]))

#
