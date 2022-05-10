from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.pack(1, 'ab'.encode(), 2.7)
# b'\x01ab@\x00\x00\x00'

# 使用类方法构造
s = Struct.__new__(Struct)
s.__init__(b'>I 2s f')
s.pack(1, 'ab'.encode(), 2.7)
# b'\x00\x00\x00\x01ab@\x00\x00\x00'

# struct模块定义的数据封装格式可以使用>、<、=或!来指定字节顺序，前面的例子都使用的是>
# 格式，它指定了字节顺序是大端（big-end
