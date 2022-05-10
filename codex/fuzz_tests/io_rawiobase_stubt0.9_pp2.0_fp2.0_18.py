import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readinto(self, b):
        n = len(b) # b will be written to from index 0
        view = memoryview(b).cast('B')
        while n > 0:
            num = self.file.readinto(view)
            view = view[num:] # slicing views is cheap
            n -= num
       return len(b) - n
        # If the object was not constructed with a BufferedIOBase
        # base, it will inherit `RawIOBase`, and the default
        # implementation of `readinto` will be used.

with open('fixture/sample.bin', 'rb') as myfile:
	 f = File(myfile)
	 b = bytearray(5)
	 f.readinto(b)
	 f.readinto(b)
	 f.close()
	 print(b)
	 #bytearray(b'\xa2\x00\xef\x00\x11\x10')
