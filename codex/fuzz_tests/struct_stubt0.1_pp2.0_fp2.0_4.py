from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# 使用struct模块来解决大数据集的问题
# 如果你的数据集中有大量的数据，那么使用struct模块来解析二进制数据会更加高效。
# 为了演示这个，假设你有一个包含1,000,000个浮点数的二进制数据块。
# 如果你使用上面的方法，那么你需要做大量的
