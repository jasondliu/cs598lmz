import lzma
lzma.decompress(_bytes=b'\xfdm\xdb\xb1(+\xe4\x01`\x10\x00\x00\x00\x03\xd1\x04\x00\x80')
</code>
Here the error "AttributeError: module 'lzma' has no attribute 'decompress' I think the module lzma should be updated because it cannot use to decompress the data.

