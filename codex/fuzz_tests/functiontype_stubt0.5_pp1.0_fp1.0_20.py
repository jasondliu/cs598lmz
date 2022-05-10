from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)

print(type(a))
print(type(b))
print(type(FunctionType))

# 生成器的一个特点是：只有在调用的时候才会生成值
# 生成器的另一个特点是：只能消费一次
# 生成器的另一个特点是：只能消费一次

# 生成器的另一个特点是：只能消费一次
# 生成器的另一个特点是：只能消费一次
# 生成器
