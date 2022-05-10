import lzma
# Test LZMADecompressor for a few compressed streams.
#
# The streams were generated with xz 5.2.2.
#
# The test files were compressed with xz --check=crc32 --compress.
#
# The test files were compressed with xz --check=crc64 --compress.
#
# The test files were compressed with xz --check=sha256 --compress.
#
# The test files were compressed with xz --check=none --compress.
#
# The test files were compressed with xz --check=crc32 --extreme --compress.
#
# The test files were compressed with xz --check=crc64 --extreme --compress.
#
# The test files were compressed with xz --check=sha256 --extreme --compress.
#
# The test files were compressed with xz --check=none --extreme --compress.
#
# The test files were compressed with xz --check=crc32 --lzma2=preset=9,dict=1MiB
# --compress.
#
# The test files were compressed with xz --check=
