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
</code>
The error is:
<code>Traceback (most recent call last):
  File "C:\Users\Владимир\Desktop\Учеба\Прога\Прога\Прога\Прога.py", line 12, in &lt;module&gt;
    f.read(1)
  File "C:\Python33\lib\io.py", line 662, in readinto
    data = self.read(n - len(bytearray))
  File "C:\Python33\lib\io.py", line 627, in read
    data = self.raw.read(self.buffer_size)
  File "C:\Users\Владимир\Desktop\Учеба\Прога\Прога\Прога\Прога.py", line 6, in read
    view = buf
NameError: name
