from types import FunctionType
a = (x for x in [1])
print(a)

b = [x for x in [1]]
print(b)

c = FunctionType
print(c)

# 总结
# 1.生成器对象是一个迭代器，可以用for循环迭代，但是不能用next()函数
# 2.生成器对象只能用一次，用过之后就没有了
# 3.生成器对象的类型是generator
# 4.生成器对象可以放到列表中，但是列表中的元素是生成器对象的内存地址
# 5.生成器对象
