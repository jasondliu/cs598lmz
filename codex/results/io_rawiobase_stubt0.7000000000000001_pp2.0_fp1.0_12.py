import io
class File(io.RawIOBase):
    def write(self, b):
        print(b)
    def close(self):
        print("closed")

f = File()
f.close()
f.write(b"hello")
f.close()
</code>
output:
<code>closed
hello
closed
</code>

