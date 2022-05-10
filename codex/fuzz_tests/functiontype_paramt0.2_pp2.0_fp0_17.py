from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# 使用生成器表达式
gen = (x for x in range(10))
gen

# 列表推导式
[x for x in range(10)]

# 字典推导式
{x: x for x in range(10)}

# 集合推导式
{x for x in range(10)}

# 字典推导式
{x: x for x in range(10)}

# 集合推导式
{x for x in range(10)}

# 字典推导式
{x: x for x in range(10)}

# 集合推导式
{x for x in range(10)}

# 字典推导式
{x: x for x in range(
