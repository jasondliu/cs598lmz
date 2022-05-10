import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to prime the pump
data = decompressor.unconsumed_tail

# Feed data to the decompressor until it needs more
while data:
    if decompressor.needs_input:
        data = input_file.read(1024)
        decompressor.feed(data)
    else:
        output_file.write(decompressor.unconsumed_tail)
        data = decompressor.unconsumed_tail

# Flush the decompressor
output_file.write(decompressor.flush())
 
# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Read one byte, just to prime the pump
data = input_file.read(1)

# Feed data to the compressor until it needs more
while data:
    if compressor.needs_input:
        data = input_file.read(1024)
        compressor.feed(data)
    else:
       
