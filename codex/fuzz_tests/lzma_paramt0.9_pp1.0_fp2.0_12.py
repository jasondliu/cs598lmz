from lzma import LZMADecompressor
LZMADecompressor().decompress("aaa".encode("utf-8"))

# compression and decompression data
with open("test.txt", "r") as file:
    content = file.read()
low_level_compressed = LZMACompressor().compress(content.encode("utf-8"))
low_level_decompressed = LZMADecompressor().decompress(low_level_compressed)
decompressed_content = low_level_decompressed.decode("utf-8")
assert content == decompressed_content
