from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<20s'
s.size = s.calcsize(s.format)

def unpack(bytestream):
    return s.unpack(bytestream)

def pack(name):
    return s.pack(name)


if __name__ == '__main__':
    import sys
    for data in sys.argv[1:]:
        print(data, unpack(data.encode('utf-8')))
