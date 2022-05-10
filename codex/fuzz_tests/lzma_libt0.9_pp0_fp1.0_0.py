import lzma
lzma.LZMAFile()
</code>
It will import it, but trying to use it does not work:
<code>python -c 'import lzma; lzma.LZMAFile()'
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
TypeError: Required argument 'filename' (pos 1) not found
</code>
Why is this happening and how can I fix it?


A:

You can't pass it to <code>LZMAFile</code> because it was built with a python version prior to 3.2, where it would not even try to look for a <code>filename</code> parameter.
It will still import, however; you can take advantage of this by providing an alias that expects a <code>filename</code> parameter.
<code>class LZMAFile(lzma.LZMAFile):
    def __new__(cls, filename):
        return super().__new__(cls, filename=filename)
</code>
Now <code>python
