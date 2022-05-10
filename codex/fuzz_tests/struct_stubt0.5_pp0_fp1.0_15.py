from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()
print(s.size)

# 二进制和其他进制的转换
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

x = 987654321
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

print(int('4d2', 16))
print(int('10011010010', 2))

# 数字的格式化输出
x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '<10.1f'))
print(format(x, '^10.1f'))
print(format(x, ','))
print(format(x, '
