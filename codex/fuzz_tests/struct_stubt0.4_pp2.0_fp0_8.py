from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x00\x00\x00\x00')

# 这个类可以用来构建和解析简单的二进制协议
# 但是，如果你想构建更复杂的协议，可能还需要使用更强大的工具。
# 比如，construct包可以让你很容易的构建复杂的二进制解析和生成器
# 另一个方面，如果你的目的是解析或者生成字节字
