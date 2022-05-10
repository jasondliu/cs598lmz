from _struct import Struct
s = Struct.__new__(Struct)
s.format = "<5x2l2HI"
s.size = calcsize(s.format)



def getChunk(self, data, offset=0, big_endian=False):
    fields = unpack_from(self.format, data, offset)
    width, height, depth, bit_field = fields[2:6]
    if big_endian:
        fieldsw = unpack('>IIII', data[offset+4:offset+16])
        width, height, depth, bit_field = fieldsw

    dx, dy = width, height
    planes = bit_field & 0xFF
    bit_count = (bit_field >> 8) & 0xFF
    compression = bit_field >> 16
    size_image = fields[6]
    size = self.size + size_image


if __name__ == '__main__':
    print('*'*20)
    print(s.size)

    #测试二进制数据格式
    t = '☻'

