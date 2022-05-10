from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 可以使用类似的方式创建其他类型的结构，如：
# Struct('>I')
# Struct('>IH')
# Struct('>IHH')
# Struct('>IHHH')
# Struct('>IHHHB')
# Struct('>IHHHBH')
# Struct('>IHHHBHH')
# Struct('>IHHHBHHH')
# Struct('>IHHHBHHHH')
# Struct('>IHHHBHHHHB')
# Struct('>IHHHBHHHHBH')
# Struct('>IHHHBHHHHBHH')
# Struct('>IHHHBHHHHBHHH')
# Struct('>IHHHBHHHHBHHHH')
# Struct('>IHHHBHHHHBHHHHB')
# Struct('>IHHHBHHHHBHHHHBH')
# Struct('>IHHHBHHHHBHHHHBHH')
# Struct('>IHHHB
