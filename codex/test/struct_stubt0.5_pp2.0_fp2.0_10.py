from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x00\x00\x00\x00')

# 反序列化
def deserialize(data):
    return json.loads(data.decode('utf-8'))

# 序列化
def serialize(data):
    return json.dumps(data).encode('utf-8')

# b'\x00\x00\x00\x00'
# b'\x00\x00\x00\x01'
# b'\x00\x00\x00\x02'
# b'\x00\x00\x00\x03'
# b'\x00\x00\x00\x04'
# b'\x00\x00\x00\x05'
# b'\x00\x00\x00\x06'
# b'\x00\x00\x00\x07'
# b'\x00\x00\x00\x08'
