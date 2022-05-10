from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('3s3sHH')

def bmp_info(data):
    # 先检查是否是BMP文件，即前两个字节是否是BM
    if data[:2] != b'BM':
        raise ValueError('not a BMP file')
    # 用struct解析数据
    all_struct = s.unpack(data[:14])
    # unpack的返回值是一个元组，把元组拆包，得到每一个字段的数据
    if all_struct[2] == 40:
        print('该位图是Windows V3位图')
