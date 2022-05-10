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
</code>

Edit:
To specifically answer your question:
<blockquote>
<p>Is it referencing the same thing? If not, how can I make it so that I can get the contents of the string after calling read(1)?</p>
</blockquote>
Yes, <code>f.read(1)</code> returns a copy of the string <code>view</code>. It's not a reference to the global variable anymore, but the Python string object is interned and thus you can still see the 'correct' data if you print the string (but because it's no longer a reference, using it as a bytearray will likely lead to problems).
If you want to be able to modify the string with file.read(), then you need to use a read() method without a size argument (If you give read() a size argument, then it returns a copy). I don't think you can do this by subclassing RawIOBase, but you can do it with <code>io.IOBase</code> (it's recommended to use it unless you have a good reason not to).
<code>import io

class File(io.IO
