import io
class File(io.RawIOBase):
    # ...
    def write(self, b):
        self.buffer.write(b)
        if b.endswith(b'\n'):
            self.flush()
</code>
This is just the simplest example I can think of, but the point is that it is entirely up to the <code>io.RawIOBase</code> subclass author to decide when and if to call <code>flush</code>.

