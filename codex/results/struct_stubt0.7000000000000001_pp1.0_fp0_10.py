from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')

with open('data.bin', 'wb') as f:
    data = s.pack(1, b'ab', 2.7)
    f.write(data)
    
with open('data.bin', 'rb') as f:
    data = f.read()
    print(s.unpack(data))
 
# 打包和解包
s = Struct('I 2s f')
with open('data.bin', 'rb') as f:
    data = f.read()
    # 返回一个元组
    print(s.unpack(data))
    # 返回一个可迭代的对象
    print(s.iter_unpack(data))
    


import struct
with open('data.bin', 'rb') as f:
    data = f.read()
    print(struct.unpack('>I 2s f', data))
    
    
    
    
    

