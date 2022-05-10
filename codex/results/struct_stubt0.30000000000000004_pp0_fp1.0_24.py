from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>HHI'
s.size = s.calcsize(s.format)

def get_data(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data

def parse_data(data):
    start = 0
    for i in range(3):
        start += 2
        length, = struct.unpack_from('>H', data, start)
        start += 2
        print(length)
        yield data[start:start+length]
        start += length

def unpack_file(filename):
    return parse_data(get_data(filename))

def main():
    for values in unpack_file(sys.argv[1]):
        print(values)

if __name__ == '__main__':
    main()
