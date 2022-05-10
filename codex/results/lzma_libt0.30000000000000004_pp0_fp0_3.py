import lzma
lzma.LZMAError: Not enough data for header
</code>
I tried to use the <code>xz</code> command line tool to decompress the file and it works fine. 
<code>xz -d file.xz
</code>
I also tried to use the <code>lzma</code> module from Python 3.4 and it works fine.
<code>import lzma
with lzma.open('file.xz', 'rb') as f:
    file_content = f.read()
</code>
I tried to use the <code>lzma</code> module from Python 2.7.6 and it doesn't work.
<code>import lzma
with lzma.open('file.xz', 'rb') as f:
    file_content = f.read()
</code>
<blockquote>
<p>lzma.LZMAError: Not enough data for header</p>
</blockquote>
I tried to use the <code>lzma</code> module from Python 2.7.8 and it doesn
