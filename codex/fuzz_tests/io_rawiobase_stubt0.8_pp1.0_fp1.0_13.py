import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name

    def read(self, size = -1):
        return 'File content'

    def readinto(self, b):
        return b'File content'

data = read_in_chunks(File('D:/Music/My.mp3'))
print(data)
</code>
In this code, I got an error:
<blockquote>
<p>TypeError: must be str, not bytes</p>
</blockquote>
How can I fix it?


A:

The issue is that in Python3 you have to use the <code>io.BytesIO</code> class for binary data.
See this answer for details.
So you should use this instead:
<code>data = read_in_chunks(io.BytesIO(b'File content'))
</code>

