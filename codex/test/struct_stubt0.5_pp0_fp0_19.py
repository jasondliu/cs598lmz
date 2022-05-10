from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')
s.size

# 使用Struct创建一个结构体类，从而可以将Python数据转换为二进制数据
s = Struct('>I')
s.pack(400)

s = Struct('>IH')
s.pack(400, 2)

# 使用packer对象的unpack()方法将二进制数据转换为Python数据
s = Struct('>IH')
s.unpack(b'\x00\x00\x01\x90\x02')

# 使用pack()和unpack()方法来处理二进制数据
with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
