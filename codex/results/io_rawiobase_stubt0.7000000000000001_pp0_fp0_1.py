import io
class File(io.RawIOBase):
    # Omitted the rest for brevity
</code>
Now I want to make a class that has the functionality of both. I know I could do <code>class File(File, io.RawIOBase)</code>, but I want it to be dynamic so that I can use <code>File</code> wherever <code>io.RawIOBase</code> is accepted.
The most obvious solution is to use multiple inheritance and make <code>File</code> inherit from <code>io.RawIOBase</code> as well:
<code>import io
class File(FileIO, io.RawIOBase):
    # Omitted the rest for brevity
</code>
This is not what I want. I want to be able to substitute <code>io.RawIOBase</code> for my custom <code>File</code> class without anything breaking. I don't want to inherit from <code>io.RawIOBase</code>.
To be more specific, I want <code>FileIO</code> to work exactly the same as <code>io.RawIOBase</code> (I don't care if there are some attributes that might
