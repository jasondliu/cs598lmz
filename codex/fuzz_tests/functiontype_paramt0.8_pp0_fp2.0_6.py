from types import FunctionType
list(FunctionType(a, {'a': 1}, 'b', None, None).__code__.__dict__.keys())

# similar to
co_varnames, co_names

# 元组
# 函数中的引用查找、方法调用、构建新元组三者是线性时间
# 字典数据类型
# 字典对键进行哈希，值可以是任何数据类型（同一字典中键和值的数据类型可以不同）
# 字典是无序的
# 字典是可变的，不能作为哈希表使用

