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
It's not even necessary to inherit from <code>io.RawIOBase</code>, the documentation says:
<blockquote>
<p>This class is also the base class for io.TextIOBase. TextIOBase adds
  unicode handling and io.BufferedIOBase adds buffering and seek(), but
  otherwise RawIOBase defines the interface that all other I/O objects
  in the hierarchy must implement.</p>
</blockquote>

