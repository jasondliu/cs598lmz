from _struct import Struct
s = Struct.__new__(Struct)
s.format = '1s3s'
print(s)
len(s.pack(*['p','y','t','h','o','n']))

def write_records(records, format, f):
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))
records = [('1.1.1.1',1),('0.0.0.0',2)]
with open('data.b', 'wb') as f:
    write_records(records, '2sI', f)
