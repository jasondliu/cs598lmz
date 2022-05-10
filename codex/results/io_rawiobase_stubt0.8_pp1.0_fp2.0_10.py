import io
class File(io.RawIOBase):  # (1)
    ...
</code>
I could not see <code>RawIOBase</code> in any of the <code>io.py</code> files on my system. Where does it come from?
(1) from http://docs.python.org/3/library/io.html
<blockquote>
<p>Note that file is not a subclass of IOBase. Use isinstance() to check
  for file objects.</p>
</blockquote>
Actually, I notice that the documentation has answer to my question:
<blockquote>
<p>FileIO(file, mode='r') ...</p>
<p>Create a FileIO object. This is a raw IO implementation of a file. It
  does not support the text I/O API. No encodings or newline
  translation is done. FileIO(file, mode='r') is equivalent to
  open(file, mode).</p>
</blockquote>
and also
<blockquote>
<p>RawIOBase ABC</p>
<p>The RawIOBase ABC defines the basic interface of raw binary I
