from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()

# Read and unpack the entire file at once
with open('data.b', 'rb') as f:
    data = f.read()

records = iter(data[i:i+s.size] for i in range(0, len(data), s.size))
for rec in records:
    print(s.unpack(rec))

# Read and unpack chunks of the file
with open('data.b', 'rb') as f:
    while True:
        data = f.read(s.size)
        if not data:
            break
        print(s.unpack(data))

# Read and unpack one record at a time
with open('data.b', 'rb') as f:
    while True:
        rec = f.read(s.size)
        if not rec:
            break
        print(s.unpack(rec))
</code>
Output:
<code>(1, b'ab', 2.7)
(2,
