import io
class File(io.RawIOBase):
    def close(self):
        do_something()
        io.RawIOBase.close(self)
</code>
This works, but you have to explicitly call <code>close()</code> (or use the context manager) to have your <code>do_something()</code> called.
You can use a context manager to hide this annoyance:
<code>class File(io.RawIOBase):
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    def close(self):
        do_something()
        io.RawIOBase.close(self)
</code>
You can now use your file as a context manager, so the file will be closed even if the function raising an exception.

