from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
s.size = calcsize(s.format)

def get_meta_data(f):
    f.seek(0)
    return s.unpack(f.read(s.size))

def get_image_data(f):
    meta_data = get_meta_data(f)
    f.seek(meta_data[3])
    return f.read()

def main():
    f = open('test.gif', 'rb')
    print(get_meta_data(f))
    print(get_image_data(f))
    f.close()

if __name__ == '__main__':
    main()
