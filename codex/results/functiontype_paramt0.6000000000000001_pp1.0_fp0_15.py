from types import FunctionType
list(FunctionType(f.func_code, f.func_globals))

# 从列表中找出最大和第二大的元素
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

max2([1, 2, 3, 4, 5, 6])

# 列表生成式
[x * x for x in range(1, 11)]

# 列表生成式中添加if条件
[x * x for x in range(1, 11) if x % 2 == 0]

# 使
