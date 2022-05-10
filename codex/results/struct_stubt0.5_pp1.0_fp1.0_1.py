from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = Struct.calcsize(s.format)

def read_int(f):
    print(f.read(s.size))
    return s.unpack(f.read(s.size))[0]

def read_data(f, size):
    return f.read(size)

def read_string(f):
    size = read_int(f)
    return read_data(f, size)

def read_file(f):
    while True:
        try:
            cmd = read_int(f)
            print(cmd)
            if cmd == 1:
                print(read_int(f))
            elif cmd == 2:
                print(read_string(f))
            elif cmd == 3:
                print(read_data(f, read_int(f)))
            elif cmd == 4:
                break
        except:
            break

def write_int(f, value):
    f.write(s.pack(value))

def write_data(
