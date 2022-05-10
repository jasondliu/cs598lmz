import mmap
# Test mmap.mmap()
class A:
    def __init__(self, filename = '/dev/null'):
        self.fp = open(filename, 'w')
        self.fp.write('abcdefghijklmnopqrstuvwxyz')

    def map(self):
        return mmap.mmap(self.fp.fileno(), 26)

    def mapto(self, start, size):
        return mmap.mmap(self.fp.fileno(), size, offset=start)

a = A()
m = a.map()
m[0]
m[1]
m[2]
m[3]
m[4]
m[5]
m[6]
m[7]
m[8]
m[9]
m[10]
m[11]
m[12]
m[13]
m[14]
m[15]
m[16]
m[17]
m[18]
m[19]
m[20]
m[21]
m[22]
m[23]
m[24
