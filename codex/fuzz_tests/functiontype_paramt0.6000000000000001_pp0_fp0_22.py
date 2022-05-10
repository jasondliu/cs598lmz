from types import FunctionType
list(FunctionType(lambda x:x,globals(),'f')(x) for x in range(3))

# 通过使用生成器表达式代替列表推导式，可以节省大量的内存
# 列表推导式会产生一个大的列表，而生成器表达式只产生一个按需生成元素的迭代器
# 下面的代码演示了如何把一个巨大的文件中的所有行连接成一个长字符串
# 如果使用一般的技术，会产生一个
