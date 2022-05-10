import _struct

def main():
    # 创建一个空的字节数组
    buffer = bytearray(12)
    # 使用struct模块的pack函数将数据打包到字节数组中
    _struct.pack_into('>ihb', buffer, 0, 1, 2, 3)
    # 将字节数组中的数据解包
    print(_struct.unpack_from('>ihb', buffer, 0))

if __name__ == '__main__':
    main()
