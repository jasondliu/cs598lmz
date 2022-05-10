from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2s2s'
s.size = s.calcsize(s.format)

def read_record(f):
    data = f.read(s.size)
    if not data:
        return None
    return s.unpack(data)

def write_record(f, name, phone):
    f.write(s.pack(name, phone))

def print_record(name, phone):
    print('{:10} {:10}'.format(name.decode('utf-8'), phone.decode('utf-8')))

def main():
    with open('phonebook.dat', 'rb') as f:
        while True:
            record = read_record(f)
            if not record:
                break
            print_record(*record)

if __name__ == '__main__':
    main()
