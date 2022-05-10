import io
class File(io.RawIOBase):
    print('Use io.RawIOBase!')
    def write(self,b):
        text = str(b)
        return text

f = File()

f.write(b'x')

print(f.write(b'x'))
</code>
I suppose the problem is with the IO not closing the file and yelling at me that the file needs to be closed first.
How do I achieve this? I would like the write function to write to the file, regardless of being opened or closed. The reason for not just opening the file is that I have other functions I wish to run, creating some kind of file buffer, as Inoob suggested in the comments.


A:

You don't create a <code>File</code> object, you create an <code>open()</code> callable:
<code>open = File
</code>
Now the <code>open()</code> builtin takes over for the new <code>File</code> callable:
<code>&gt;&gt;&gt; open.__dict__
mappingproxy({'__class__': &lt
