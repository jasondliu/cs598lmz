from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('bb')
s.pack(1, 2)

import struct
struct.pack('bb', 1, 2)

# 如果你曾经使用过使用下面这种方法来初始化Struct对象，那么你可能会很惊讶：
s = Struct('bb')

# 这个问题源于 Struct 是一个类，而不是一个工厂函数或者其他形式的简单接口。 尽管在某些地方它看上去像一个函数，但是它实际上是一个类。
# 因此，它
