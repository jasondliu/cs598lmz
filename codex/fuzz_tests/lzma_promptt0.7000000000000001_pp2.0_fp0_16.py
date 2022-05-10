import lzma
# Test LZMADecompressor
# The decompressor object decompresses data incrementally.
dec = lzma.LZMADecompressor()
with open('enwik8', 'rb') as f:
    # Read chunks of data from the file and feed them into the decompressor.
    # When you have no more data to give to the decompressor, call the
    # flush() method to flush the internal buffers of the decompressor.
    for chunk in iter(lambda: f.read(10 * 1024 * 1024), b''):
        data = dec.decompress(chunk)
        print(len(data))

#        # Write the uncompressed data.
#        with open('enwik8_lzma_decomp', 'ab') as g:
#            g.write(data)

# Finish compression.
data = dec.flush()
print(len(data))
#with open('enwik8_lzma_decomp', 'ab') as g:
#    g.write(data)



#print(dec.unused_data)

#print(dec.eof)
