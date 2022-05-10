import lzma
lzma.decompress(open('save1.txt','rb').read())

# b'I tried to use a callback, but it was not working.Then I checked the x64 assembly of gzip.py and I saw that my callback didnt set the writable flag.After I saw it, I had found EPyTools again and made a script for editing the flags for gzip.py.Thanks for your time, hope it helps.'
</code>
Decompressed:
<code>I tried to use a callback, but it was not working.Then I checked the x64 assembly of gzip.py and I saw that my callback didn't set the writable flag.After I saw it, I had found EPyTools again and made a script for editing the flags for gzip.py.Thanks for your time, hope it helps.
</code>

