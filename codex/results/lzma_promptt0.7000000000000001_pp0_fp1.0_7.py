import lzma
# Test LZMADecompressor
compressor = lzma.LZMADecompressor()
buf = bytearray()
while True:
    chunk = bz2File.read(1024)
    if not chunk: break
    buf += compressor.decompress(chunk)

print(buf[0:100])

import bz2
# Test BZ2Decompressor
compressor = bz2.BZ2Decompressor()
buf = bytearray()
while True:
    chunk = bz2File.read(1024)
    if not chunk: break
    buf += compressor.decompress(chunk)

print(buf[0:100])
</code>
Output
<code>b'&lt;?xml version="1.0" encoding="utf-8"?&gt;\n&lt;s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"&gt;\n  &lt;s:Body&gt;\n    &lt;GetAdsResponse xmlns='http://adcenter.microsoft
