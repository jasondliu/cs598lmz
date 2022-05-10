import bz2
bz2_output = bz2.BZ2Compressor(9, fp=bz2_file)

print("Reading %d bytes" %(text_len))
with open(text_file, 'rb') as fp:
    buf = fp.read()
    print("Writing %d bytes" %(len(buf)))
    bz2_output.write(buf)
    bz2_output.flush()

print("Closing BZ2Compressor object")
bz2_output.close()

print("Closing compressed file")
bz2_file.close()

print("Opening compressed file and decompressing")
bz2_file = bz2.BZ2File(compressed_file, 'rb')
bz2_input = bz2.BZ2Decompressor()
bz2_data = bz2_input.decompress(bz2_file.read())
print("After decompression: %d bytes" %(len(bz2_data)))
print("After decompression: %d bytes" %(len(b
