from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.unpack(b'\x00\x00\x00\x01')

# 如果你只是想打包和解包某些基本类型的数据，那么使用 struct 模块会非常方便。
# 但是如果你要处理的是复杂的二进制格式，或者你想构造自定义的格式，那么使用 struct 就会有些困难。
# 这时候你可能会考虑使用自己写的字节码解析器或者其
