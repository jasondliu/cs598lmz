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
which fails on Python 3.5 but works on Python 3.6 (and presumably newer versions) with the following error message:
<blockquote>
<pre><code>&lt;code&gt;&amp;gt;&amp;gt;&amp;gt; import io
&amp;gt;&amp;gt;&amp;gt; import weakref
&amp;gt;&amp;gt;&amp;gt; view = None
&amp;gt;&amp;gt;&amp;gt; class File(io.RawIOBase):
...     def readinto(self, buf):
...         global view
...         view = buf
...     def readable(self):
...         return True
... 
&amp;gt;&amp;gt;&amp;gt; f = io.BufferedReader(File())
&amp;gt;&amp;gt;&amp;gt; f.read(1)
b''
&amp;gt;&amp;gt;&amp;gt; del f
&amp;gt;&amp;gt;&amp;gt; view
&
