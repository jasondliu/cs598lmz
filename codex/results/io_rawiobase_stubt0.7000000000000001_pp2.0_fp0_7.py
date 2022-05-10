import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b"bytes"
f = File()
print(f.read())
f.close()

# 如果你没有文件名，但是想使用一个临时文件，那么你可以使用 tempfile.TemporaryFile 来创建一个。
import tempfile
with tempfile.TemporaryFile() as f:
    f.write(b'hello world\n')
    f.write(b'Testing\n')

    f.seek(0)
    data = f.read()
    print(data)

# 如果你想创建一个命名的临时文件，可以使用 tempfile.NamedTemporaryFile() 函数来创建一个，你可以通
