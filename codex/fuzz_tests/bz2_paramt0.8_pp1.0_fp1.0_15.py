from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed)

print("s1:", len(s1), "s2:", len(s2))

# s1: 2495434 s2: 2475049

#  the LZMA protocol is less coarse-grained than the LZMA file format.
# The LZMA file format is based on the XZ file format, and the XZ file format is based on the LZMA2 file format
# https://tukaani.org/lzma/benchmarks.html
# The stream compression formats .lzma (LZMA/LZMA2) and .xz (.lzma2) are based on the LZMA2 format.
# The .xz file format is an improved version of the LZMA2 format.
# The .lzma format uses the legacy LZMA2 format, which does not support stream integrity check and encoder delay
# The .lzma format is a legacy format that can contain only a single file.
# The .xz format supports multiple files and other features like CRC32, CRC64, and SHA-256 checksums, integrity
