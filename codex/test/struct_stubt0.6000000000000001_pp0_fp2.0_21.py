from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(b'!i')
s.pack(42)

# Struct.__new__(Struct)
# Struct.__init__(s, b'!i')
# Struct.pack(s, 42)

# 注意：在 Python 中，通常不需要显式地调用 __new__ ，因为默认的 __new__ 方法在 __init__ 方法被调用之前正确地创建了实例。
# 但是，你构建自定义的元类时，你可能会需要定制 __new__ 方法。

# 当自定义 __new__ 时，要注意调用
