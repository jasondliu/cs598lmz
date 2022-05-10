import io
class File(io.RawIOBase):
    def __init__(self, fileName):
        self.file = io.open(fileName, "r+b")

    def read(self, n = -1):
        return self.file.read(n)

    def write(self, b):
        return self.file.write(b)

    def seek(self, offset, whence = io.SEEK_SET):
        self.file.seek(offset, whence)

    def close(self):
        self.file.close()

class Image(File):
    def __init__(self, fileName):
        File.__init__(self,fileName)
        self.read(2)
        self.width = read_word(self.file)
        self.height = read_word(self.file)
        self.pixels = []
        for y in xrange(self.height):
            self.pixels.append([])
            for x in xrange(self.width):
                pixel = read_dword(self.file)
                self.pixels[y].append(pixel)
       
