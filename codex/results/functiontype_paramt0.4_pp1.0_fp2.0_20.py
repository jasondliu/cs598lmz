from types import FunctionType
list(FunctionType(lambda x:x,globals()) for x in range(5))

# 生成器表达式
gen = (x for x in range(5))
print(type(gen))

# 生成器函数
def gen_fun():
    for x in range(5):
        yield x

print(type(gen_fun()))

# 列表推导式
print([x for x in range(5)])

# 字典推导式
print({x:x for x in range(5)})

# 集合推导式
print({x for x in range(5)})

# 生成器推导式
print((x for x in range(5)))

# 列表推导式
print([x for x in range(5)])

# 字典推导式
print({
