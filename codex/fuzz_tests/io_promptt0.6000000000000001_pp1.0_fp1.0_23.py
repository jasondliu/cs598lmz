import io
# Test io.RawIOBase
rawiobase = io.RawIOBase()
rawiobase.read([1])
rawiobase.readall()
rawiobase.readinto(b'\x00')
rawiobase.readinto1(b'\x00')
rawiobase.readinto([b'\x00'])
rawiobase.readline()
rawiobase.readlines()
rawiobase.seek(1, 2)
rawiobase.truncate()
rawiobase.truncate(1)
rawiobase.writable()
rawiobase.write(b'\x00')
rawiobase.write([b'\x00'])
rawiobase.writelines([b'\x00'])

# Test io.RawIOBase with a buffer
rawiobase = io.RawIOBase()
rawiobase.read([1], [1])
rawiobase.read1([1], [1])
rawiobase.readinto([b'\x00'], [1])

