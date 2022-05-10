fn = lambda: None
# Test fn.__code__.co_flags
# fn.__code__.co_flags = 0
# # 二进制表示
# print(fn.__code__.co_flags) # 0b100000
# # 十进制表示
# print(fn.__code__.co_flags) # 32

# 全局变量，用于保存变量名
# fn.__code__.co_names = ('a', 'b')

# 全局变量，保存类型或者函数名
# fn.__code__.co_varnames = ('fn', 'var')

# 保存函数参数名
# fn.__code__.co_varnames = ('a', 'b', 'c')

# 全局变量，保存局部变量
