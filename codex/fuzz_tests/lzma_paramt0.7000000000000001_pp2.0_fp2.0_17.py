from lzma import LZMADecompressor
LZMADecompressor().decompress(request.content)
</code>
However, it throws the following error:
<code>Traceback (most recent call last):
File "lzmafile.py", line 11, in &lt;module&gt;
LZMADecompressor().decompress(request.content)
File "/usr/lib/python3.5/lzma.py", line 275, in decompress
return self.decompressobj.decompress(data)
lzma.LZMAError: Input format not supported
</code>
What do I need to do to decode the content?


A:

You need to read the first byte of the file to determine the LZMA properties.
See the source code.
<code>import lzma
import requests

request = requests.get('https://www.python.org/static/img/python-logo.png.lzma')

# https://www.7-zip.org/sdk.html
props = request.content[:5]
size = request.content[5:9]


