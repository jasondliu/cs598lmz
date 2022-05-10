import lzma
lzma.LZMAError

class LZMAFile(GenericFile):
    def __init__(self, f):
        self.file = f
        self.decompressor = lzma.LZMADecompressor()

    def read(self, size):
        return self.decompressor.decompress(self.file.read(size))


class OpenSSLFile(GenericFile):
    def __init__(self, f):
        self.file = f
        self.decryptor = AES.new(b'password', AES.MODE_EAX, nonce=b'12345678')

    def read(self, size):
        return self.decryptor.decrypt(self.file.read(size))

with LZMAFile(io.BytesIO(os.urandom(100))) as f:
    print(f.read())

with OpenSSLFile(io.BytesIO(os.urandom(100))) as f:
    print(f.read())
