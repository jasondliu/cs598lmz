from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('enwiki-20161101-pages-articles-multistream.xml.bz2', 'rb').read())
</code>
Also, I tried to use the below code, but it gives me an error:
<code>with bz2.open('enwiki-20161101-pages-articles-multistream.xml.bz2', 'rb') as f:
    file_content = f.read()
</code>
Error:
<code>Traceback (most recent call last):
  File "C:\Users\Desktop\Desktop\wiki\wiki.py", line 4, in &lt;module&gt;
    with bz2.open('enwiki-20161101-pages-articles-multistream.xml.bz2', 'rb') as f:
  File "C:\Users\AppData\Local\Programs\Python\Python36\lib\bz2.py", line 293, in open
    fileobj = _builtin_open(filename, mode + "b")
PermissionError: [Errno 13] Permission denied: 'en
