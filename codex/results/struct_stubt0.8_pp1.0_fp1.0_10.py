from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size
def write_records(records, format, f):
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))
records = [(1, 2.3, 4.5),
           (6, 7.8, 9.0),
           (12, 13.4, 56.7)]
with open('data.bin', 'wb') as f:
    write_records(records, '<idd', f)
with open('data.bin', 'rb') as f:
    data = f.read()
data
s.unpack_from(data, 0)
s.unpack_from(data, s.size)
s.unpack_from(data, 2*s.size)
