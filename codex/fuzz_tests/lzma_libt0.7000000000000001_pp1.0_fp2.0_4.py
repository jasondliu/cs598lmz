import lzma
lzma.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')
# b'Hello'
</code>
This is the header of the xz file:
<code>---
- xz
  - block
    - header
      - block_size: 32
      - block_uncompressed_size: 5
      - block_checksum: 0x9a9a9a9a
      - total_size: 31
      - flags:
        - is_compressed: True
        - is_compressed_with_lzma2: True
        - has_crc32: True
        - has_uncompressed_size: True
      - compression_method: 2
      - filter_flags:
        - lzma2_dict_size: 0x04000000
        - lzma2_mode: 1
        - lzma2_
