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

img = QImage(view, width, height, bytesPerLine=bytesPerLine, format=QImage.Format_Grayscale8)
img.save('/tmp/test.jpg', format='JPG')
