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
gc.collect()
print(view, type(view))
</code>
output:
<code>&gt;&gt;&gt; import gc, io
&gt;&gt;&gt; class File(io.RawIOBase):
...     def readinto(self, buf):
...         global view
...         view = buf
...     def readable(self):
...         return True
...
&gt;&gt;&gt; f = io.BufferedReader(File())
&gt;&gt;&gt; f.read(1)
&gt;&gt;&gt; del f
&gt;&gt;&gt; gc.collect()
&lt;captured buffer for 0x7fddccbbf240, size 1, obj 0x7fddcc9aa098 at 0x7fddccbbf240&gt; &lt;class 'memoryview'&gt;
</code>
You can remedy the leak by deleting the global reference:
<code>&gt;&gt;&gt; del view
&gt;&gt;&gt;
