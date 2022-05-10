import lzma
# Test LZMADecompressor

compressor = lzma.LZMADecompressor()

with open('../models/en-de/en-de.src.en.bpe.lzma', 'rb') as f_in:
    with open('../models/en-de/en-de.src.en.bpe.lzma.out', 'wb') as f_out:
        for chunk in iter(lambda: f_in.read(1024 * 1024), b''):
            f_out.write(compressor.decompress(chunk))
 
# Test LZMACompressor

compressor = lzma.LZMACompressor()

with open('../models/en-de/en-de.src.en.bpe.lzma.out', 'rb') as f_in:
    with open('../models/en-de/en-de.src.en.bpe.lzma.out.lzma', 'wb') as f_out:
        for chunk in iter(lambda: f_in.read(1024 * 1024), b''):
           
