from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('hhl', 'abc')
s.size

# 以下是输出结果:
# >>> from _struct import Struct
# >>> s = Struct.__new__(Struct)
# >>> s.__init__('hhl', 'abc')
# >>> s.size
# 8
