from types import FunctionType
a = (x for x in [1])
len(a)

some_list = ['a','b','c','b','d','m','n','n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)

# 用reduce求最大值
nums = [1,2,3,4,5,6,7]
result = reduce(lambda x,y:x if x>y else y,nums)
result

# 三元表达式
# 条件为真时返回的结果 if 条件判断 else 条件为假时的返回结果
# 一般用在条件判断简单
x = 1
y = 100
result = x if x<y else y
result

# 迭代器
# 可以被
