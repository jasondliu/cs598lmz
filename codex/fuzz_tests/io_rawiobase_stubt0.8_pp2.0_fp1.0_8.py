import io
class File(io.RawIOBase):
    def readline(self):
        return b'line\n'

f = File()
print(f.readable())     # Return True because this class was derived from a Raw IO class
print(f.readline())     # Call readline function of Raw IO class
print(f.readlines())    # Call readlines function of Raw IO class
f = File()
print(f.read(5))        # Call read function of Raw IO class (read 5 raw bytes)
print(f.read(10))       # Call read function of Raw IO class (read 10 raw bytes)
f = File()
for line in f:          # Call read function of Raw IO class (read 5 raw bytes)
    print(line)
class File(io.TextIOBase):
    def readline(self):
        return 'line\n'

f = File()
print(f.readline())     # Call readline function of Text IO class (read one line)
print(f.readlines())    # Call readlines function of Text IO class (read all lines)
f = File()
print(f.read(5
