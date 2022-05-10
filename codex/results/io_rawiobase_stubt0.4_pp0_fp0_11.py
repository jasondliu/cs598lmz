import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = io.open(name, 'rb')

    def readable(self):
        return True

    def readinto(self, b):
        return self.file.readinto(b)
</code>
I then use this class as follows
<code>from my_file import File

with File("/tmp/file.txt") as f:
    for line in f:
        print(line.decode("utf-8"))
</code>
The problem is that the <code>for</code> loop is never entered. I know that the file is being opened correctly because I can read from it using <code>readinto</code> directly.
I have also tried using <code>io.BufferedReader</code> instead of <code>io.RawIOBase</code> in the <code>File</code> class. This still does not work.
What am I doing wrong?


A:

The problem was that I was not implementing the <code>__iter__</code> method.
The following code works
