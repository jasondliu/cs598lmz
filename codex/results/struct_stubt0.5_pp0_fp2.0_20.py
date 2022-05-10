from _struct import Struct
s = Struct.__new__(Struct)
s.format = "I"
s.size = 4

def write_record(record, format, f):
    f.write(s.pack(*record))

def read_records(format, f):
    records = []
    while True:
        r = s.unpack(f.read(s.size))
        if r:
            records.append(r[0])
        else:
            break
    return records

if __name__ == '__main__':
    records = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    with open('data.b', 'wb') as f:
        for record in records:
            write_record(record, format, f)
    with open('data.b', 'rb') as f:
        print(read_records(format, f))
