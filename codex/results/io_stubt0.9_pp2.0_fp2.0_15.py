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
view.release_buffers()
view = None
gc.collect()
print('ok')
""")

# Issue #9110: when a BufferedIOBase.close() method was leaking a reference to
# the underlying raw IO object, a call to the raw object close() method after
# closing all BufferedIOBase objects would segfault.
add_docstring(io.BufferedReader.close, "\n")
add_docstring(io.BufferedWriter.close, "\n")
add_docstring(io.BufferedRwpair.close, "\n")

# Issue #3770: if the BufferedReader.read() runs into a UnicodeDecodeError
# when it tries to decode the binary data read from the raw stream, it should
# fall back to the 'replace' error handler.
import _io
_io.IncrementalNewlineDecoder.error_handler = 'replace'

# Issue #14947: tp_print for BufferedReader/BufferedWriter treated objects as
# having no readable/writable buffer.
_io._IOBase.__buffer__ = property(
