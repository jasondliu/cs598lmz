import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

print(view)
print(view[0])
print(view[1])
print(view[2])
print(view[3])
print(view[4])
print(view[5])
print(view[6])
print(view[7])
print(view[8])
print(view[9])
print(view[10])
print(view[11])
print(view[12])
print(view[13])
print(view[14])
print(view[15])
print(view[16])
print(view[17])
print(view[18])
print(view[19])
print(view[20])
print(view[21])
print(view[22])
print(view[23])
print(view[24])
print(view[25])
print(view[26])
print(view[27])
print(view[28])
print(view[29])
print(view[30])
print(view[31])
print(view[32])
print(view[33])
print(view[34])
