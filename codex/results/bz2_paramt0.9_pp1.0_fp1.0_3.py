from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_content)
</code>
It works fine in my linux environment but once I started working in windows environment, I realized that this causes issues at the point where there is an extra carriage return in the content. Below is an example of the content that I am trying to compress.
<code>compressed_content = 'BZh9\x04\x00\x00\x01\x03\x00@\x00\x1f\x00\x01\x00\x00\x00Pi\x89\x00\x08\x0c\x00\x989\xc9\x18\x00\x00\x00(\x03\x00\x09\x00\x05\x00\x00\x00\xe8\x8f\x03\x95\xbcE \x00\r\x00\x00\x00\x00\x008\xa1\xd1\xcd\xe6n\xa8M\x00%\xc9\x86\xf1\xa5\x01\x02\
