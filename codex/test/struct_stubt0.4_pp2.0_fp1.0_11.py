from _struct import Struct
s = Struct.__new__(Struct)
print(s)

# 注意：
# Struct.__new__() 只是调用了 Struct.__init__()，并且没有返回值。
# 因此，返回的是 Struct.__init__() 方法的返回值 None。
