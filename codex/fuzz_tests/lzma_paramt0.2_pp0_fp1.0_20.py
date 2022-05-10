from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# lzma.LZMAError: Input format not supported by decoder
</code>
I've tried to use <code>xz</code> to decompress the file, but it doesn't work:
<code>$ xz -d -v -k -T0 -9 -e file.xz

file.xz:
  File type:           XZ
  Compressed data:     7.7%
  Uncompressed size:   8.0 MiB
  Compressed size:     7.4 MiB
  Uncompressed checksum:  CRC32
  Compressed checksum:    CRC64
  Compression ratio:   1.05
  Compression options:
    Dictionary size:   64 KiB
    Block size:        64 KiB
    Filters:           LZMA2
    Check:             CRC64
    Flags:             EOS
  Decompression options:
    Flags:             EOS
  Decompressed:        100%

xz: (stdin): Unexpected end of input
</code>
I've tried to
