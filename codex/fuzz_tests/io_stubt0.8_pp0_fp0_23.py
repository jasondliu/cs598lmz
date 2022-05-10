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
del view
</code>
The above prints the value <code>'o'</code>, which is what I expected. However, I can't find any documentation which guarantees the result.
Is it safe to use the <code>buf</code> parameter from any function which takes it beyond that function's scope?


A:

The docs do say:
<blockquote>
<p>The returned object is an instance of a class that adds buffering to the
  underlying raw stream. Its <code>&lt;code&gt;read()&lt;/code&gt;</code>, <code>&lt;code&gt;readinto()&lt;/code&gt;</code> and <code>&lt;code&gt;readline()&lt;/code&gt;</code> methods
  will buffer data in order to operate efficiently. The optional <code>&lt;code&gt;buffer_size&lt;/code&gt;</code>
  argument specifies the size in bytes of the buffer to be used.</p>
</blockquote>
So it's safe to hold a
