import types
types.MethodType(func, num) # 将num和函数func关联起来
"""
"""

# 别名
"""
v = float('inf')
a = v
a = 1
v # 结果还是 inf
"""

# 序列切片
"""
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four:', a[:4])
print('Last four:', a[-4:])

# 序列切片省略开始角标
print('Middle two:', a[3:-3])
"""

# 增加切片步长
"""
print('b' in a) # 列表是否包含某个值
print(a[::2]) # 奇数位
print(a[::-1]) #
