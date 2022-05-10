from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))

# 二进制
bin(10)
int('0b1010', 2)

# 八进制
oct(10)
int('0o12', 8)

# 十六进制
hex(10)
int('0xa', 16)

# 其他进制
int('1010', 2)
int('12', 8)
int('a', 16)

# 按位运算符
# 按位与
# 对于每一个比特位，只有两个操作数都是1时，结果才是1，否则就是0
print(bin(0b1110 & 0b101))

# 按位或
# 对于每一个比特位
