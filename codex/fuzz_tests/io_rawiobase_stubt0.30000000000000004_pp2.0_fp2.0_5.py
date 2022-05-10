import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = os.open(name, os.O_WRONLY | os.O_CREAT)
    def write(self, b):
        return os.write(self.fd, b)
    def close(self):
        return os.close(self.fd)

# f = File('/tmp/junk.txt')
# f.write(b'0123456789abcdef')
# f.close()
# print(open('/tmp/junk.txt', 'rb').read())
# os.remove('/tmp/junk.txt')

# f = open('/tmp/junk.txt', 'w')
# f.write('0123456789abcdef')
# f.close()
# print(open('/tmp/junk.txt', 'rb').read())
# os.remove('/tmp/junk.txt')

# f = open('/tmp/junk.txt', 'wb')
# f.write(b'01234567
