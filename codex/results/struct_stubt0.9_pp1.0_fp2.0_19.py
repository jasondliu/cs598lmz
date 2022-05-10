from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size
s = Struct('I 2s f')
s.size
s = Struct('I 2s f')
data = s.pack(12345, b'xy', 67.8)
data
s.unpack(data)
(12345, b'xy', 67.8)
data_str = 'This is my data string'.encode()
data_str.split()
'This is my data string'.split()
[i for i in 'This is my data string' if i.isalpha()]
'This is my data string'.split()[0]
'This is my data string'.split()[0].encode()
type(b'this')
'This is my data string'.encode().split()
b'This is my data string'.split()
b'This is my data string'.decode(encoding='utf-8').split()
import os
os.path.basename('/etc/hosts')
os.path.basename('/etc/hosts'.encode())
os.path.basename
