import lzma
lzma.decompress(open("files/files.tar.lzma", "rb").read())

import lz4.block
lz4.block.decompress(open("files/files.tar.lz4", "rb").read())

import brotli
brotli.decompress(open("files/files.tar.br", "rb").read())

import zstandard as zstd
zstd.ZstdDecompressor().decompress(open("files/files.tar.zstd", "rb").read())
