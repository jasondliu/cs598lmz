from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

data = s.pack(1, 'ab'.encode('utf-8'), 2.7)
data

s.unpack(data)

# 使用struct模块来解决字节对齐问题
import os

def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)

if os.path.exists('data.b'):
    os.remove('data.b')

with open('data.b',
