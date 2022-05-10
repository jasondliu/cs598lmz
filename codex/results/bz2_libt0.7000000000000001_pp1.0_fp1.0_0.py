import bz2
bz2.decompress(f)
</code>
but I get the following error:
<code>UnicodeDecodeError: 'utf-8' codec can't decode byte 0xdc in position 1: invalid continuation byte
</code>
Running <code>file</code> on the file shows that it's a <code>bzip2 compressed data</code> file. How can I read this file with Python?


A:

Use the <code>bz2.open()</code> context manager to read BZ2 files as a text stream:
<code>with bz2.open(fp, mode='rt', encoding='utf8') as f:
    for line in f:
        print(line)
</code>
You can use <code>f.read()</code> to read the entire file into memory, or read the file line by line as I did.
If you want a binary file, use <code>mode='rb'</code>.
Demo:
<code>&gt;&gt;&gt; import bz2
&gt;&gt;&gt; fp = b
