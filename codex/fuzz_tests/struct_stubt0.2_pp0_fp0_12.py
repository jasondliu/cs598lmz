from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# 这个例子中，我们首先创建一个空的结构体对象，然后使用 __init__() 方法去初始化它。
# 然后，我们使用 unpack() 方法将一个字节字符串转换成一个元组。
# 如果你想将一个结构体变量转换成一个字节字符串，你可以使用 pack() 方法，比如：

s = Struct('
