from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 注意：这里的 Struct 并不是 _struct 模块的 Struct 类，
# 而是一个类工厂函数，用于创建结构化的数据类型。

# 可以通过类工厂函数创建的类型，具有与 _struct 模块中的 Struct 类型相同的方法。
# 例如，可以使用 pack() 和 unpack() 方法对数据进行编码和解码。

# 下面是一个简单的例子
