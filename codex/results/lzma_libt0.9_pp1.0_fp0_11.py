import lzma
lzma.LZMADecompressor.decompress(b).decode()
# 'The quick brown fox jumps over the lazy dog.'
</code>
Alternatively, let's convert XZ to a safe <code>.xz</code> format, and pipe it in to <code>xzcat</code>:
<code>import lzma
from subprocess import check_output
check_output('cd $(mktemp -d) &amp;&amp; base64 -di &gt; file.xz &amp;&amp; xzcat file.xz',
             input=b'eJztWUlT0lMzVQQAZ4Lh9s4sabDAdxaeZLuHpzCwqavXLqPFzVCg7VNGcdKI0jKb20i2B1OJlVxGnU6R+U6QJUAKmAA='   ,
             shell=True, text=True)
# 'The quick brown fox jumps over the lazy dog.'
</code>

