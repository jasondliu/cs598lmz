from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 内置的struct模块可以解决字节序问题，但是不适合大量数据的处理
# 如果你需要操作大量的二进制数据，可以考虑使用numpy模块
# 它提供了类似的结构化数组功能
import numpy as np
# 数组的内容是32位整数，每个整数占4个字节
# 数组的第一个元素是一个头部，用来存
