import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

with open('compressed/sample.bz2', 'rb') as f, open('compressed/output_bz2.txt', 'wb') as o:
    file_content = f.read()
    data = decompressor.decompress(file_content)
    o.write(data)
# Test BZ2Compressor
compressor = bz2.BZ2Compressor(9)

with open('compressed/input.txt', 'rb') as f, open('compressed/output_bz2.bz2', 'wb') as o:
    while True:
        file_chunk = f.read(1000000)
        if not file_chunk:
            break
        o.write(compressor.compress(file_chunk))
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()

with open('compressed/sample.xz', 'rb') as f, open('compressed/output_xz.txt
