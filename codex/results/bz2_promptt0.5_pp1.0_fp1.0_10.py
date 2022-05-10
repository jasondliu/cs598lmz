import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('/home/ubuntu/workspace/tensorflow/tensorflow/examples/how_tos/reading_data/text_0.txt.bz2', 'rb') as f:
    file_content = f.read()
    uncompressed_data = decompressor.decompress(file_content)
    print(uncompressed_data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('/home/ubuntu/workspace/tensorflow/tensorflow/examples/how_tos/reading_data/text_0.txt', 'rb') as f:
    file_content = f.read()
    compressed_data = compressor.compress(file_content)
    compressed_data += compressor.flush()
    print(compressed_data)

# Test BZ2File

with bz2.BZ2File('/home/ubuntu/workspace/tensorflow/tensorflow/examples/
