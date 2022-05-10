import lzma
lzma.LZMAError: Input format was not recognized
</code>
I don't know what's wrong.
I tried to <code>os.system</code> a lzma command, and it works fine:
<code>&gt;&gt;&gt; os.system('lzma -zc test.txt &gt; output.lzma')
0
</code>
But I still need to load the <code>output.lzma</code> file in Python.
I am using a Mac OS X 10.6.8 and Python 2.7.1, and I installed <code>lzma</code> with <code>pip</code>.


A:

The <code>lzma</code> module doesn't support reading LZMA/XZ files, only writing them.  You'll need to use the <code>xz</code> module, which does support reading them.

