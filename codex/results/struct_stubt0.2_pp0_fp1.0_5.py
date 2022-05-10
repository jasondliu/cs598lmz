from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 可以使用类方法来创建结构，而不需要显式的实例化
Struct.__new__.__defaults__ = (None,)
Struct('>i')

# 可以使用类方法来创建结构，而不需要显式的实例化
Struct.__new__.__defaults__ = (None,)
Struct('>i')

# 可以使用类方法来创建结构，而不需要显式的实例化
Struct.__new__.__defaults__ = (None,)
Struct('>i')

# 可以使用类方法来
