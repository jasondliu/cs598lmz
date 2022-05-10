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
print(view.__array_interface__)

# $ python3.7 -c 'from _testcapi import get_buffer_view, get_buffer_ptr; print(get_buffer_view(get_buffer_ptr(b"abc".__array_interface__)))'
# b'abc'
# b'abc'
# $ python3.7 -c 'from _testcapi import get_buffer_view, get_buffer_ptr; print(get_buffer_view(get_buffer_ptr(b"abc".__array_interface__, 0)))'
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# ValueError: Buffer has been released
# $ python3.7 -c 'from _testcapi import get_buffer_view, get_buffer_ptr; print(get_buffer_view(get_buffer_ptr(b"abc".__array_interface__, 1)))'
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# Value
