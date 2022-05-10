import ctypes

class S(ctypes.Structure):
    x = 0

spam = S()

# 内存地址, 成员的偏移量
print(id(spam), '---', ctypes.addressof(spam))
print(id(spam.x), '---', ctypes.addressof(spam) + ctypes.sizeof(ctypes.c_int))

# 将数据从网络上获取解析

print('---------------------------------------------------------------------------------------------------------')


# 输出
# 140204151279728 --- 140177990751776
# 140204151279696 --- 140177990751792
